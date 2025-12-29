---

# 📖 FIDO2‑Key‑Manager

A simple graphical user interface (GUI) tool for managing **FIDO2 security keys** (YubiKey, Feitian, Token2, TrustKey, SoloKey, etc.).

Originally built for **Fedora Linux**, but works seamlessly on **Arch Linux**, **CachyOS**, and **Ubuntu / KDE Neon** with the right dependencies installed.

<img width="598" height="429" alt="Screenshot" src="https://github.com/user-attachments/assets/5dd84d69-84d7-4f75-860d-ed99ec7a7dc6" />

---

## 🎯 Project Purpose

FIDO2 keys are powerful for authentication, but managing them from the command line can be confusing.  
**FIDO2‑Key‑Manager** provides a lightweight GTK interface to make common tasks easier:

- 🔍 View connected FIDO2 devices  
- 📑 Display device information  
- 🔐 Manage resident credentials (passkeys)  
- 🔄 Change or reset PINs  
- 🧹 Perform factory resets (irreversible)  
- 🖥️ Run sensitive operations in a separate `xterm` window for clarity and safety  

---

## ✨ Features

- Clean GTK‑based GUI  
- Tooltips and dialogs for user guidance  
- Uses `fido2-token` from `libfido2`  
- Secure PIN entry via `xterm`  
- No background daemons or services required  

---

## 📦 Prerequisites

| Distro                | Packages to Install                                                                 |
|-----------------------|--------------------------------------------------------------------------------------|
| **Fedora**            | `sudo dnf install xterm python3-fido2 python3-gobject gtk3`                          |
| **Arch / CachyOS**    | `sudo pacman -S xterm libfido2 python-gobject gtk3`                                 |
| **Ubuntu / KDE Neon** | `sudo apt install xterm python3-fido2 python3-gi libgtk-3-0 fido2-tools`            |

### Ubuntu / KDE Neon Notes

Run the application from the project directory:

```bash
python3 fido2_gui.py
```

(Optional):

```bash
chmod +x fido2_gui.py
./fido2_gui.py
```

---

## 🚀 Installation & Usage

# 🔹 Arch / CachyOS

```bash
git clone https://github.com/kev2600/FIDO2-Key-Manager.git
cd FIDO2-Key-Manager
makepkg -si
```

Launch:

```bash
fido2-key-manager
```

---

# 🔹 Fedora

### Install prerequisites

```bash
sudo dnf install xterm python3-fido2 python3-gobject gtk3
sudo dnf install rpm-build rpmdevtools
```

### Set up the RPM build tree

```bash
rpmdev-setuptree
```

### Clone the repository

```bash
git clone https://github.com/kev2600/FIDO2-Key-Manager.git
cd FIDO2-Key-Manager
```

### Build the source tarball (automatic version detection)

```bash
VERSION=$(rpmspec -q --qf "%{VERSION}\n" fido2-key-manager.spec)
git archive --format=tar.gz --prefix=fido2-key-manager-$VERSION/ HEAD \
  > ~/rpmbuild/SOURCES/fido2-key-manager-$VERSION.tar.gz
```

### Build the RPM

```bash
rpmbuild -ba fido2-key-manager.spec
```

### Install the generated RPM

```bash
sudo dnf install ~/rpmbuild/RPMS/noarch/fido2-key-manager-$VERSION-1.fc$(rpm -E %fedora).noarch.rpm
```

Launch:

```bash
fido2-key-manager
```

---

## 🛡️ Security Notes

- PIN changes and factory resets require interactive confirmation in a separate `xterm` window.  
- Factory reset is **irreversible** — all credentials on the key will be wiped.  
- Always install dependencies from official repositories.  

---

## 🧪 Test Your FIDO2 Key

You can create a test resident credential using a WebAuthn demo site:

https://webauthn.io

Works with every FIDO2 key.

---

## 🍏 Experimental macOS Support

macOS includes full support for FIDO2 devices through `libfido2`, and the Python FIDO2 library works as well.  
The GTK3 GUI *should* run on macOS using Homebrew, but this is **experimental**.

### Install dependencies

```bash
brew install python3 libfido2 gtk+3 pygobject3
```

### Run the application

```bash
python3 fido2_gui.py
```

If you try this on macOS, please open an Issue with your results.

---

## 📜 License

Distributed under the **GPL‑3.0** license.  
Free to use, modify, and share under the same terms.

---
- add a **GitHub Actions release workflow**  

Just tell me what direction you want next.
