Name:           fido2-key-manager
Version:        1.1
Release:        1%{?dist}
Summary:        GUI tool for managing FIDO2 security keys on Linux

License:        GPL-3.0-or-later
URL:            https://github.com/kev2600/FIDO2-Key-Manager
Source0:        %{name}.tar.gz

BuildArch:      noarch

Requires:       python3-gobject
Requires:       gtk3
Requires:       libfido2
Requires:       fido2-tools
Requires:       xterm

%description
FIDO2 Key Manager is a simple GTK-based graphical tool for managing
FIDO2 security keys (YubiKey, TrustKey, etc.) on Linux using libfido2.

Features:
- List connected devices
- View device info
- Change PIN
- List resident credentials (passkeys)
- Factory reset (with safety warnings)
- Secure PIN entry via xterm

%prep
%autosetup

%build
# Nothing to build - pure Python

%install
install -Dm755 fido2_gui.py %{buildroot}%{_bindir}/fido2-key-manager
install -Dm644 fido2-key-manager.desktop %{buildroot}%{_datadir}/applications/fido2-key-manager.desktop
install -Dm644 fido2-key-manager.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/fido2-key-manager.png

%files
%{_bindir}/fido2-key-manager
%{_datadir}/applications/fido2-key-manager.desktop
%{_datadir}/icons/hicolor/512x512/apps/fido2-key-manager.png

%changelog
* Mon Dec 29 2025 kev2600 <your-email-if-you-want@example.com> - 1.1-1
- Major UI improvements:
  + Modern grid layout and better spacing
  + Auto-select first detected device
  + Status indicator ("Ready" when device selected)
  + Colored output log (info/blue, error/red, warning/orange)
  + Significantly safer factory reset flow with detailed warnings
  + Guided terminal prompts for physical reset steps
  + Red destructive-action button for reset

* [Previous entry if any - or this is the first]
- Initial package
