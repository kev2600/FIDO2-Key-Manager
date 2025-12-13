# 📖 FIDO2‑Key‑Manager

A simple graphical user interface (GUI) tool for managing **FIDO2 security keys** (such as YubiKeys, Feitian, Token2, or other hardware tokens).  

This project was originally built for **Fedora Linux**, but it also works seamlessly on **Arch Linux** and **CachyOS** with the right dependencies installed.

---

## 🎯 Project Purpose
FIDO2 keys are powerful for authentication, but managing them from the command line can be intimidating.  
**FIDO2‑Key‑Manager** provides a lightweight GTK interface to make common tasks easier:

- 🔍 View connected FIDO2 devices  
- 📑 Display device information  
- 🔐 Manage credentials stored on the key  
- 🔄 Change or reset PINs  
- 🧹 Perform factory resets (irreversible)  
- 🖥️ Run interactive operations in a separate terminal (`xterm`) for security and clarity  

---

## ✨ Features
- Clean GTK‑based GUI  
- Tooltips and dialogs for user guidance  
- Uses `fido2-token` under the hood (from `libfido2`)  
- Independent terminal (`xterm`) for PIN entry and resets  

---

## 📦 Prerequisites

| Distro         | Packages to Install                                                                 |
|----------------|--------------------------------------------------------------------------------------|
| **Fedora**     | `sudo dnf install xterm python3-fido2 python3-gobject gtk3`                          |
| **Arch/CachyOS** | `sudo pacman -S xterm libfido2 python-gobject gtk3`                                 |

Notes:
- **Fedora**: `python3-fido2` provides the FIDO2 library and CLI tools. On Fedora Workstation, `python3-gobject` and `gtk3` are usually preinstalled, but they’re listed here for completeness.  
- **Arch/CachyOS**: `libfido2` includes the CLI tools (`fido2-token`, `fido2-cred`). `python-gobject` and `gtk3` are required for the GTK GUI.  
- **xterm**: Used for PIN entry and factory reset prompts in a separate terminal window.  

---

## 🚀 Installation & Usage

```bash
# Clone the repo
git clone https://github.com/kev2600/FIDO2-Key-Manager.git
cd FIDO2-Key-Manager

# Run the GUI
python3 fido2_gui.py
```

---

## 🛡️ Security Notes
- PIN changes and factory resets require interactive confirmation.  
- Factory reset is **irreversible** — all credentials on the key will be wiped.  
- Always download dependencies from official repositories to avoid tampered software.  

---

## 📜 License
Distributed under the **GPL‑3.0 license**.  
Free to use, modify, and share under the same terms.
