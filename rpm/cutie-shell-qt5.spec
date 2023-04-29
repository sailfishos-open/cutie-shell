%{?opt_qt5_default_filter}

Summary: Mobile UI inspired by Jolla SailfishOS
Name: cutie-shell-qt5
Version: 0.0.1
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: GPLv3
Url:     https://cutie-shell.org/
Source0: %{name}-%{version}.tar.bz2

BuildRequires: systemd
BuildRequires: make
BuildRequires: opt-qt5-qtbase-devel >= 5.15
BuildRequires: pkgconfig(zlib)
BuildRequires: opt-qt5-qtbase-private-devel
BuildRequires: opt-qt5-qtdeclarative-devel >= 5.15
Requires:      opt-qt5-qtbase-gui >= 5.15
Requires:      opt-qt5-qtvirtualkeyboard
Requires:      qml-module-cutie

%description
Cutie Shell aims to be a pretty and easy-to-use mobile UI/UX for Linux devices running
either Halium or mainline Linux. Our UI is inspired by Jolla’s Sailfish OS, but we are
not aiming for a clone. One major difference to Saifish OS is that our source is
completely open.

%prep
%autosetup -n %{name}-%{version}/upstream


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%{opt_qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

%files
/etc/systemd/logind.conf.d/10-cutie.conf
%{_bindir}/cutie-ui-io
%{_unitdir}/cutie-ui-io.service
%{_datadir}/atmospheres/Current/wallpaper.jpg
%{_datadir}/atmospheres/air/wallpaper.jpg
%{_datadir}/atmospheres/airy/wallpaper.jpg
%{_datadir}/atmospheres/aurora/wallpaper.jpg
%{_datadir}/atmospheres/city/wallpaper.jpg
%{_datadir}/atmospheres/night/wallpaper.jpg
%{_datadir}/cutie-keyboard/layouts/en_US/CtrlKey.qml
%{_datadir}/cutie-keyboard/layouts/en_US/EscKey.qml
%{_datadir}/cutie-keyboard/layouts/en_US/TabKey.qml
%{_datadir}/cutie-keyboard/layouts/en_US/WSpaceKey.qml
%{_datadir}/cutie-keyboard/layouts/en_US/dialpad.qml
%{_datadir}/cutie-keyboard/layouts/en_US/digits.qml
%{_datadir}/cutie-keyboard/layouts/en_US/handwriting.qml
%{_datadir}/cutie-keyboard/layouts/en_US/main.qml
%{_datadir}/cutie-keyboard/layouts/en_US/numbers.qml
%{_datadir}/cutie-keyboard/layouts/en_US/symbols.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/CtrlKey.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/EscKey.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/TabKey.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/WSpaceKey.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/dialpad.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/digits.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/handwriting.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/main.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/numbers.qml
%{_datadir}/cutie-keyboard/layouts/fi_FI/symbols.qml
