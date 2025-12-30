Name:           fido2-key-manager
Version:        1.1
Release:        1%{?dist}
Summary:        GUI tool for managing FIDO2 security keys on Linux

License:        GPL-3.0-or-later
URL:            https://github.com/kev2600/FIDO2-Key-Manager
Source0:        %{name}-%{version}.tar.gz

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
%setup -q

%build
# Nothing to build for Python + icons
echo "Nothing to build"

%install
# Install main script
install -Dm755 fido2_gui.py %{buildroot}%{_bindir}/fido2-key-manager

# Install desktop entry
install -Dm644 fido2-key-manager.desktop \
    %{buildroot}%{_datadir}/applications/fido2-key-manager.desktop

# Install icons
for size in 16 24 32 48 64 128 256 512; do
    install -Dm644 icons/hicolor/${size}x${size}/apps/fido2-key-manager.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/fido2-key-manager.png
done

%files
%license LICENSE
%{_bindir}/fido2-key-manager
%{_datadir}/applications/fido2-key-manager.desktop
%{_datadir}/icons/hicolor/*/apps/fido2-key-manager.png

%changelog
* Tue Dec 30 2025 Kevin <you@example.com> - 1.1-1
- Initial RPM release
