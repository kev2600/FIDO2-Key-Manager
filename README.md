# FIDO2-Key-Manager
FIDO2-Key-Manager - a Fedora GUI to manage FIDO2 Keys.

#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
import subprocess
import shutil

class Fido2Manager(Gtk.Window):
    def __init__(self):
        super().__init__(title="FIDO2 Key Manager")
        self.set_border_width(10)
        self.set_default_size(600, 400)

        # Vertical Box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Device List
        self.device_store = Gtk.ListStore(str)
        self.device_combo = Gtk.ComboBox.new_with_model(self.device_store)
        renderer_text = Gtk.CellRendererText()
        self.device_combo.pack_start(renderer_text, True)
        self.device_combo.add_attribute(renderer_text, "text", 0)
        self.device_combo.set_tooltip_text("Select a FIDO2 device")
        vbox.pack_start(self.device_combo, False, False, 0)

        # Buttons
        btn_list = Gtk.Button(label="List Devices")
        btn_list.connect("clicked", self.list_devices)
        btn_list.set_tooltip_text("Refresh connected FIDO2 devices")
        vbox.pack_start(btn_list, False, False, 0)

        btn_info = Gtk.Button(label="Device Info")
        btn_info.connect("clicked", self.device_info)
        btn_info.set_tooltip_text("Show info of selected device")
        vbox.pack_start(btn_info, False, False, 0)

        btn_passkeys = Gtk.Button(label="List Passkeys")
        btn_passkeys.connect("clicked", self.list_passkeys)
        btn_passkeys.set_tooltip_text("Open terminal to list passkeys (requires PIN)")
        vbox.pack_start(btn_passkeys, False, False, 0)

        btn_change_pin = Gtk.Button(label="Change PIN")
        btn_change_pin.connect("clicked", self.change_pin)
        btn_change_pin.set_tooltip_text("Change device PIN interactively")
        vbox.pack_start(btn_change_pin, False, False, 0)

        btn_factory_reset = Gtk.Button(label="Factory Reset")
        btn_factory_reset.connect("clicked", self.factory_reset)
        btn_factory_reset.set_tooltip_text("Factory reset device (irreversible)")
        vbox.pack_start(btn_factory_reset, False, False, 0)

        btn_clear = Gtk.Button(label="Clear Output")
        btn_clear.connect("clicked", self.clear_output)
        btn_clear.set_tooltip_text("Clear the output log below")
        vbox.pack_start(btn_clear, False, False, 0)

        # Output TextView
        self.output = Gtk.TextView()
        self.output.set_editable(False)
        self.output_buffer = self.output.get_buffer()
        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.output)
        scrolled.set_vexpand(True)
        vbox.pack_start(scrolled, True, True, 0)

    # ----- Helper Methods -----
    def append_output(self, text):
        GLib.idle_add(lambda: self.output_buffer.insert(self.output_buffer.get_end_iter(), text + "\n"))

    def clear_output(self, widget):
        self.output_buffer.set_text("")

    def run_command(self, cmd, capture_output=True):
        try:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=capture_output, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"

    def get_selected_device(self):
        tree_iter = self.device_combo.get_active_iter()
        if tree_iter is not None:
            return self.device_store[tree_iter][0].split(":")[0]
        else:
            self.append_output("No device selected!")
            return None

    # ----- Button Actions -----
    def list_devices(self, widget):
        output = self.run_command("fido2-token -L")
        self.device_store.clear()
        for line in output.splitlines():
            self.device_store.append([line])
        self.append_output("Devices:\n" + output)

    def device_info(self, widget):
        device = self.get_selected_device()
        if device:
            cmd = f"fido2-token -I '{device}'"
            output = self.run_command(cmd)
            self.append_output("Device Info:\n" + output)

    def list_passkeys(self, widget):
        device = self.get_selected_device()
        if not device:
            return
        cmd = f"fido2-token -L -r {device}"

        # Check for xterm
        if shutil.which("xterm") is None:
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text="xterm not found",
            )
            dialog.format_secondary_text(
                "Please install xterm to use this feature:\n"
                "Fedora: sudo dnf install xterm\n"
                "Debian/Ubuntu: sudo apt install xterm"
            )
            dialog.run()
            dialog.destroy()
            return

        # Open xterm for interactive PIN entry
        self.append_output("--- List Passkeys ---")
        self.append_output(f"Running in xterm: {cmd}")
        subprocess.run(f"xterm -e '{cmd}; echo Press Enter to close; read'", shell=True)

    def change_pin(self, widget):
        device = self.get_selected_device()
        if device:
            self.append_output("Changing PIN (interactive)...")
            subprocess.run(f"xterm -e 'fido2-token -C {device}; echo Press Enter to close; read'", shell=True)

    def factory_reset(self, widget):
        device = self.get_selected_device()
        if device:
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.WARNING,
                buttons=Gtk.ButtonsType.OK_CANCEL,
                text="Factory Reset",
            )
            dialog.format_secondary_text("This action is irreversible. Continue?")
            response = dialog.run()
            dialog.destroy()
            if response == Gtk.ResponseType.OK:
                self.append_output("Factory reset (interactive)...")
                subprocess.run(f"xterm -e 'sudo fido2-token -R {device}; echo Press Enter to close; read'", shell=True)

# ----- Run App -----
win = Fido2Manager()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
