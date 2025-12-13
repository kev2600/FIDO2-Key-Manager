Name:           fido2-key-manager
Version:        1.0.0
Release:        1%{?dist}
Summary:        GTK GUI for managing FIDO2 security keys

License:        GPLv3+
URL:            https://github.com/kev2600/FIDO2-Key-Manager
Source0:        https://github.com/kev2600/FIDO2-Key-Manager/archive/refs/heads/master.tar.gz

BuildArch:      noarch

Requires:       python3
Requires:       python3-fido2
Requires:       python3-gobject
Requires:       gtk3
Requires:       xterm

%description
FIDO2 Key Manager is a lightweight GTK GUI for managing FIDO2 security keys
(YubiKey, Feitian, Token2, etc). It provides a user-friendly interface for
viewing devices, managing credentials, changing PINs, and performing resets.

%prep
%setup -q

%build
# Nothing to build, pure Python

%install
# Install the Python script
install -Dm755 fido2_gui.py %{buildroot}%{_bindir}/fido2-key-manager

# Install the desktop entry
install -Dm644 fido2-key-manager.desktop \
    %{buildroot}%{_datadir}/applications/fido2-key-manager.desktop

# Install the icon
install -Dm644 fido2-key-manager.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/fido2-key-manager.png

%files
%license LICENSE
%doc README.md
%{_bindir}/fido2-key-manager
%{_datadir}/applications/fido2-key-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/fido2-key-manager.png

%changelog
* Fri Dec 12 2025 Kev <you@example.com> - 1.0.0-1
- Initial RPM release
