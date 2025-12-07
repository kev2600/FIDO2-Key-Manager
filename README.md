## 📖 README Summary: FIDO2-Key-Manager
- **Project Purpose:**  
  A graphical user interface (GUI) tool for **Fedora Linux** that helps users manage **FIDO2 security keys** (like YubiKeys or other hardware tokens).

- **Features (from README):**
  - Provides a simple GUI for interacting with FIDO2 keys.  
  - Likely supports operations such as:
    - Viewing connected keys  
    - Managing credentials stored on the key  
    - Resetting or configuring keys  

- **Installation / Usage:**  
  The README suggests cloning the repository and running the Python script:
  ```bash
  sudo dnf install xterm
  git clone https://github.com/kev2600/FIDO2-Key-Manager.git
  cd FIDO2-Key-Manager
  python3 fido2_gui.py

  ```
  Since it’s Fedora-focused, you may need to install dependencies via `dnf` or `pip` (e.g., `python3-fido2`, GTK or PyQt libraries depending on the GUI framework used).

- **License:**  
  Distributed under **GPL-3.0**, meaning it’s open-source and free to modify/share under the same license.
