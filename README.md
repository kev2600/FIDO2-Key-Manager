# 📖 FIDO2‑Key‑Manager

**FIDO2‑Key‑Manager** is a lightweight, open, cross‑distro GUI utility designed for administrators, support teams, and technically inclined users who need a reliable way to recover or reset FIDO2 security keys. Its purpose is simple: take a key in an unknown or unusable state and restore it to a clean, working condition — without relying on vendor‑specific software.

The tool is implemented entirely in **Python**, using **GTK** and **standard open libraries**, with no proprietary components. It is intentionally minimal and vendor‑agnostic, focusing on the essential operations needed to rescue a key from any manufacturer, including YubiKey, Feitian, Token2, TrustKey, SoloKey, and others.

Originally developed for Fedora Linux, it also runs smoothly on Arch Linux, CachyOS, Ubuntu, and KDE Neon when the appropriate dependencies are installed.

<img width="683" height="547" alt="Screenshot_20251230_163045" src="https://github.com/user-attachments/assets/137a617f-0d64-47bd-947e-c22455b90bfb" />


---

## 🎯 Project Purpose

Recovering or resetting a FIDO2 key often requires vendor‑specific utilities — if they exist at all.  
**FIDO2‑Key‑Manager** is built for the opposite scenario: when you *don’t* have the vendor’s software, when the key’s state is unknown, or when you simply need to wipe it and start fresh.

The tool is designed for cross‑distro use (work in progress) and aims to provide a universal, open, vendor‑agnostic rescue workflow:

- plug in a FIDO2 key from **any vendor**,  
- on **any Linux system**,  
- with **no proprietary tools**,  
- and **reset it back to a known‑good state**.

To support that mission, the tool provides:

- 🔄 **Change or reset the key’s PIN**  
- 🧹 **Perform a full factory reset** — wiping the device and deleting all resident keys  
- 📑 **Display a complete hardware information dump** (via `fido2-token`)  
- 🔍 **List resident keys (discoverable credentials)** stored on the authenticator  

The tool can **enumerate** resident keys but does **not** provide selective management (adding, editing, or deleting individual credentials). The only destructive action is the full factory reset, which clears everything on the device.

In short:  
**FIDO2‑Key‑Manager is a cross‑distro, open, vendor‑agnostic rescue utility for bringing any FIDO2 key back to a clean, usable state.**

---

## ✨ Features

- Clean, minimal GTK‑based interface  
- Built entirely with Python and standard open libraries  
- Uses `fido2-token` from `libfido2`  
- Secure PIN entry handled through `xterm`  
- No background daemons or services required  
- Designed for cross‑distro compatibility (work in progress)  

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

- PIN changes and factory resets require explicit confirmation in a separate `xterm` window.  
- Factory reset is **permanent** — all credentials on the key will be erased.  
- Always install dependencies from official repositories.  

---

## 🧪 Test Your FIDO2 Key

You can test your key using the WebAuthn demo site:

https://webauthn.io

---

## 🍏 Experimental macOS Support

macOS provides full support for FIDO2 devices through libfido2, and the Python FIDO2 library works normally as long as the required dependencies are installed.
The GTK3 GUI can run on macOS via Homebrew, but this remains experimental and may require additional setup.
Install dependencies

```bash
brew install python3 libfido2 gtk+3 pygobject3
brew install xterm
brew install --cask xquartz

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
