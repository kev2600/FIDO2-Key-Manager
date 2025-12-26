```markdown
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

| Distro              | Packages to Install                                                                 |
|---------------------|--------------------------------------------------------------------------------------|
| **Fedora**          | `sudo dnf install xterm python3-fido2 python3-gobject gtk3`                          |
| **Arch/CachyOS**    | `sudo pacman -S xterm libfido2 python-gobject gtk3`                                 |
| **Ubuntu / KDE Neon** | `sudo apt update && sudo apt install xterm python3-fido2 python3-gi libgtk-3-0 fido2-tools` |

### Ubuntu / KDE Neon Notes
Run the application from the project directory:

```bash
python3 fido2_gui.py



Notes:
- **Fedora**: `python3-fido2` provides the FIDO2 library and CLI tools. On Fedora Workstation, `python3-gobject` and `gtk3` are usually preinstalled, but they’re listed here for completeness.  
- **Arch/CachyOS**: `libfido2` includes the CLI tools (`fido2-token`, `fido2-cred`). `python-gobject` and `gtk3` are required for the GTK GUI.  
- **xterm**: Used for PIN entry and factory reset prompts in a separate terminal window.  

---

## 🚀 Installation & Usage

### 🔹 Arch / CachyOS
```bash
# Clone the repo
git clone https://github.com/kev2600/FIDO2-Key-Manager.git
cd FIDO2-Key-Manager

# Build and install using PKGBUILD
makepkg -si
```

After installation, launch the app from your application menu or by running:
```bash
fido2-key-manager
```

---

### 🔹 Fedora

```bash
# Install prerequisites
sudo dnf install xterm python3-fido2 python3-gobject gtk3
sudo dnf install rpm-build rpmdevtools

# Set up the RPM build tree
rpmdev-setuptree

# Clone the repo (in your home directory)
git clone https://github.com/kev2600/FIDO2-Key-Manager.git
cd FIDO2-Key-Manager

# Copy the spec file into SPECS
cp fido2-key-manager.spec ~/rpmbuild/SPECS/

# Prepare the source tarball (exclude .git, name must match spec)
cd ..
cp -r FIDO2-Key-Manager fido2-key-manager-1.0.0
tar czvf ~/rpmbuild/SOURCES/master.tar.gz --exclude='.git' fido2-key-manager-1.0.0

# Build the RPM
rpmbuild -ba ~/rpmbuild/SPECS/fido2-key-manager.spec

# Install the generated RPM (note the Fedora release tag, e.g. fc43)
sudo dnf install ~/rpmbuild/RPMS/noarch/fido2-key-manager-1.0.0-1.fc$(rpm -E %fedora).noarch.rpm
```

After installation, launch the app from your application menu or by running:
```bash
fido2-key-manager
```

---

## 🛡️ Security Notes
- PIN changes and factory resets require interactive confirmation in a separate `xterm` window.  
- Factory reset is irreversible — all credentials on the key will be wiped.  
- Always download dependencies from official repositories to avoid tampered software.  

---

## 📜 License
Distributed under the GPL‑3.0 license.  
Free to use, modify, and share under the same terms.
```

---
