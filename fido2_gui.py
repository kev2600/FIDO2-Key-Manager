#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Pango
import subprocess
import shutil

class Fido2Manager(Gtk.Window):
    def __init__(self):
        super().__init__(title="FIDO2 Key Manager")
        self.set_border_width(15)
        self.set_default_size(680, 520)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.add(vbox)

        # Device selection
        device_box = Gtk.Box(spacing=8)
        vbox.pack_start(device_box, False, False, 0)

        label = Gtk.Label()
        label.set_markup("<b>Select Device:</b>")
        device_box.pack_start(label, False, False, 0)

        self.device_store = Gtk.ListStore(str)
        self.device_combo = Gtk.ComboBox.new_with_model(self.device_store)
        renderer_text = Gtk.CellRendererText()
        self.device_combo.pack_start(renderer_text, True)
        self.device_combo.add_attribute(renderer_text, "text", 0)
        device_box.pack_start(self.device_combo, True, True, 0)

        self.status_label = Gtk.Label()
        self.status_label.set_markup("<i>No device connected</i>")
        vbox.pack_start(self.status_label, False, False, 0)

        # Buttons grid
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(8)
        vbox.pack_start(grid, False, False, 0)

        buttons = [
            ("List Devices", self.list_devices),
            ("Device Info", self.device_info),
            ("List Passkeys", self.list_passkeys),
            ("Change PIN", self.change_pin),
            ("Factory Reset", self.factory_reset),
            ("Clear Output", self.clear_output),
        ]

        for i, (label, callback) in enumerate(buttons):
            btn = Gtk.Button(label=label)
            btn.connect("clicked", callback)
            if label == "Factory Reset":
                btn.get_style_context().add_class("destructive-action")
            grid.attach(btn, i % 2, i // 2, 1, 1)

        # Output
        self.output = Gtk.TextView()
        self.output.set_editable(False)
        self.output.modify_font(Pango.FontDescription("Monospace 10"))
        self.output_buffer = self.output.get_buffer()

        scrolled = Gtk.ScrolledWindow()
        scrolled.add(self.output)
        scrolled.set_vexpand(True)
        vbox.pack_start(scrolled, True, True, 0)

    def append_output(self, text, tag=None):
        GLib.idle_add(lambda: self.output_buffer.insert_with_tags_by_name(
            self.output_buffer.get_end_iter(), text + "\n", tag or "normal"))

    def clear_output(self, widget):
        self.output_buffer.set_text("")

    # Your original run_command — keeps detection working
    def run_command(self, cmd, capture_output=True):
        try:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=capture_output, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"

    def get_selected_device(self):
        tree_iter = self.device_combo.get_active_iter()
        if tree_iter is not None:
            return self.device_store[tree_iter][0].split(":")[0].strip()
        return None

    def update_status(self, text):
        GLib.idle_add(lambda: self.status_label.set_markup(text))

    # Your original list_devices — proven to work with your key
    def list_devices(self, widget):
        output = self.run_command("fido2-token -L")
        self.device_store.clear()
        if not output:
            self.append_output("No FIDO2 devices found.", "error")
            self.update_status("<i>No device connected</i>")
            return
        for line in output.splitlines():
            self.device_store.append([line])
        self.append_output("Devices:\n" + output, "info")
        self.device_combo.set_active(0)  # Auto-select first
        self.update_status("<span foreground='#4CAF50'><b>Ready</b></span>")

    # Rest with polish
    def device_info(self, widget):
        device = self.get_selected_device()
        if device:
            output = self.run_command(f"fido2-token -I '{device}'")
            self.append_output("Device Info:\n" + output, "info")

    def list_passkeys(self, widget):
        device = self.get_selected_device()
        if not device:
            return
        if shutil.which("xterm") is None:
            # simple dialog
            dialog = Gtk.MessageDialog(transient_for=self, message_type=Gtk.MessageType.ERROR, buttons=Gtk.ButtonsType.OK, text="xterm not found")
            dialog.format_secondary_text("Install xterm: sudo dnf install xterm")
            dialog.run()
            dialog.destroy()
            return
        self.append_output("--- List Passkeys (PIN required) ---", "info")
        subprocess.run(f"xterm -e 'fido2-token -L -r {device}; echo Press Enter to close; read'", shell=True)

    def change_pin(self, widget):
        device = self.get_selected_device()
        if device:
            self.append_output("Changing PIN (interactive)...", "info")
            subprocess.run(f"xterm -e 'fido2-token -C {device}; echo Press Enter to close; read'", shell=True)

    def factory_reset(self, widget):
        device = self.get_selected_device()
        if not device:
            return

        dialog = Gtk.MessageDialog(
            transient_for=self,
            message_type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.NONE,
            text="<big><b>Factory Reset – IRREVERSIBLE</b></big>",
        )
        dialog.format_secondary_markup(
            "<b>All data will be erased!</b>\n\n"
            "PIN, passkeys, and configuration gone forever.\n"
            "You'll need to re-register everywhere.\n\n"
            "<b>Process:</b> Remove key → Reinsert → Touch within 10s"
        )
        dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)
        reset_btn = dialog.add_button("Perform Reset", Gtk.ResponseType.OK)
        reset_btn.get_style_context().add_class("destructive-action")

        response = dialog.run()
        dialog.destroy()

        if response == Gtk.ResponseType.OK:
            self.append_output("Factory reset starting — follow terminal!", "warning")
            subprocess.run(
                f"xterm -title 'Factory Reset' -e "
                f"'echo \"REMOVE key now...\"; read; "
                f"sudo fido2-token -R {device}; "
                f"echo \"Done if successful. Press Enter.\"; read'",
                shell=True
            )
            GLib.timeout_add_seconds(3, self.list_devices, None)

# Tags for color
def setup_tags(buffer):
    buffer.create_tag("normal")
    buffer.create_tag("info", foreground="#2196F3", weight=Pango.Weight.BOLD)
    buffer.create_tag("error", foreground="#F44336", weight=Pango.Weight.BOLD)
    buffer.create_tag("warning", foreground="#FF9800", weight=Pango.Weight.BOLD)

win = Fido2Manager()
win.connect("destroy", Gtk.main_quit)
setup_tags(win.output_buffer)
win.show_all()
Gtk.main()
