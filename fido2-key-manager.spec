Name:           fido2-key-manager
Version:        1.1
Release:        1%{?dist}
Summary:        GUI utility to manage and reset FIDO2 security keys

License:        GPL-3.0-or-later
URL:            https://github.com/kev2600/FIDO2-Key-Manager
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(fido2)
BuildRequires:  python3dist(pygobject)
BuildRequires:  gtk3
BuildRequires:  desktop-file-utils

Requires:       python3
Requires:       python3dist(fido2)
Requires:       python3dist(pygobject)
Requires:       gtk3
Requires:       xterm

%description
FIDO2-Key-Manager is a lightweight GTK utility for resetting or recovering
FIDO2 security keys from any vendor.

%prep
%autosetup

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

install -m 0755 fido2_gui.py %{buildroot}%{_bindir}/fido2-key-manager
install -m 0644 fido2-key-manager.desktop %{buildroot}%{_datadir}/applications/
install -m 0644 icons/256x256/fido2-key-manager.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

%files
%license LICENSE
%{_bindir}/fido2-key-manager
%{_datadir}/applications/fido2-key-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/fido2-key-manager.png

%changelog
Prep for package review
