pkgname=fido2-key-manager
pkgver=1.0.0
pkgrel=1
pkgdesc="GTK GUI for managing FIDO2 security keys"
arch=('any')
url="https://github.com/kev2600/FIDO2-Key-Manager"
license=('GPL3')
depends=('python-gobject' 'gtk3' 'libfido2' 'xterm')
source=("fido2_gui.py"
        "fido2-key-manager.desktop"
        "fido2-key-manager.png")
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
  cd "$srcdir"

  # Install the Python script
  install -Dm755 fido2_gui.py "$pkgdir/usr/bin/fido2-key-manager"

  # Install the .desktop file
  install -Dm644 fido2-key-manager.desktop \
    "$pkgdir/usr/share/applications/fido2-key-manager.desktop"

  # Install the icon
  install -Dm644 fido2-key-manager.png \
    "$pkgdir/usr/share/icons/hicolor/256x256/apps/fido2-key-manager.png"
}
