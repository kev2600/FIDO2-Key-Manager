FIDO2‑Key‑Manager

FIDO2‑Key‑Manager is a lightweight, open, cross‑distro GUI utility designed for administrators, support teams, and technically inclined users who need a reliable way to recover or reset FIDO2 security keys. Its purpose is simple: take a key in an unknown or unusable state and restore it to a clean, working condition — without relying on vendor‑specific software.

The tool is implemented entirely in Python, using GTK and standard open libraries, with no proprietary components. It is intentionally minimal and vendor‑agnostic, focusing on the essential operations needed to rescue a key from any manufacturer, including YubiKey, Feitian, Token2, TrustKey, SoloKey, and others.

Originally developed for Fedora Linux, it also runs smoothly on Arch Linux, CachyOS, Ubuntu, and KDE Neon when the appropriate dependencies are installed.

<img width="598" height="429" alt="Screenshot" src="https://github.com/user-attachments/assets/5dd84d69-84d7-4f75-860d-ed99ec7a7dc6" />
🎯 Project Purpose

Recovering or resetting a FIDO2 key often requires vendor‑specific utilities — if they exist at all.
FIDO2‑Key‑Manager is built for the opposite scenario: when you don’t have the vendor’s software, when the key’s state is unknown, or when you simply need to wipe it and start fresh.

The tool is designed for cross‑distro use (work in progress) and aims to provide a universal, open, vendor‑agnostic rescue workflow:

    plug in a FIDO2 key from any vendor,

    on any Linux system,

    with no proprietary tools,

    and reset it back to a known‑good state.

To support that mission, the tool provides:

    🔄 Change or reset the key’s PIN

    🧹 Perform a full factory reset — wiping the device and deleting all resident keys

    📑 Display a complete hardware information dump (via fido2-token)

    🔍 List resident keys (discoverable credentials) stored on the authenticator

The tool can enumerate resident keys but does not provide selective management (adding, editing, or deleting individual credentials). The only destructive action is the full factory reset, which clears everything on the device.

In short:
FIDO2‑Key‑Manager is a cross‑distro, open, vendor‑agnostic rescue utility for bringing any FIDO2 key back to a clean, usable state.
