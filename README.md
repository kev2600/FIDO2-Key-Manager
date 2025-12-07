📖 FIDO2-Key-Manager


🎯 Project Purpose
A graphical user interface (GUI) tool for Fedora Linux that helps users manage FIDO2 security keys (such as YubiKeys or other hardware tokens).

✨ Features
Simple GUI for interacting with FIDO2 keys

Supports operations like:

Viewing connected keys

Managing credentials stored on the key

Resetting or configuring keys

🚀 Installation & Usage
 ```bash
# Install prerequisites
sudo dnf install xterm python3-fido2

# Clone the repo
git clone https://github.com/kev2600/FIDO2-Key-Manager.git
cd FIDO2-Key-Manager

# Run the GUI
python3 fido2_gui.py
```


  Since it’s Fedora-focused, you may need to install dependencies via `dnf` or `pip` (e.g., `python3-fido2`, GTK or PyQt libraries depending on the GUI framework used).

Distributed under the GPL-3.0 license. Free to use, modify, and share under the same terms.
