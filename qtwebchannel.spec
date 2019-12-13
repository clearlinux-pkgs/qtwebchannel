#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtwebchannel
Version  : 5.14.0
Release  : 19
URL      : https://download.qt.io/official_releases/qt/5.14/5.14.0/submodules/qtwebchannel-everywhere-src-5.14.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.14/5.14.0/submodules/qtwebchannel-everywhere-src-5.14.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtwebchannel-lib = %{version}-%{release}
Requires: qtwebchannel-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5WebSockets)
BuildRequires : pkgconfig(Qt5Widgets)

%description
A REPL client for any qwebchannel service using a websocket transport.
A nice tool for testing qwebchannel endpoints.

%package dev
Summary: dev components for the qtwebchannel package.
Group: Development
Requires: qtwebchannel-lib = %{version}-%{release}
Provides: qtwebchannel-devel = %{version}-%{release}
Requires: qtwebchannel = %{version}-%{release}

%description dev
dev components for the qtwebchannel package.


%package lib
Summary: lib components for the qtwebchannel package.
Group: Libraries
Requires: qtwebchannel-license = %{version}-%{release}

%description lib
lib components for the qtwebchannel package.


%package license
Summary: license components for the qtwebchannel package.
Group: Default

%description license
license components for the qtwebchannel package.


%prep
%setup -q -n qtwebchannel-everywhere-src-5.14.0
cd %{_builddir}/qtwebchannel-everywhere-src-5.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1576219667
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtwebchannel
cp %{_builddir}/qtwebchannel-everywhere-src-5.14.0/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtwebchannel/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtwebchannel-everywhere-src-5.14.0/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/qtwebchannel/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/qtwebchannel-everywhere-src-5.14.0/LICENSE.GPL3 %{buildroot}/usr/share/package-licenses/qtwebchannel/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/qtwebchannel-everywhere-src-5.14.0/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtwebchannel/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtwebchannel-everywhere-src-5.14.0/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtwebchannel/f45ee1c765646813b442ca58de72e20a64a7ddba
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtWebChannel/5.14.0/QtWebChannel/private/qmetaobjectpublisher_p.h
/usr/include/qt5/QtWebChannel/5.14.0/QtWebChannel/private/qqmlwebchannelattached_p.h
/usr/include/qt5/QtWebChannel/5.14.0/QtWebChannel/private/qwebchannel_p.h
/usr/include/qt5/QtWebChannel/5.14.0/QtWebChannel/private/signalhandler_p.h
/usr/include/qt5/QtWebChannel/5.14.0/QtWebChannel/private/variantargument_p.h
/usr/include/qt5/QtWebChannel/QQmlWebChannel
/usr/include/qt5/QtWebChannel/QWebChannel
/usr/include/qt5/QtWebChannel/QWebChannelAbstractTransport
/usr/include/qt5/QtWebChannel/QtWebChannel
/usr/include/qt5/QtWebChannel/QtWebChannelDepends
/usr/include/qt5/QtWebChannel/QtWebChannelVersion
/usr/include/qt5/QtWebChannel/qqmlwebchannel.h
/usr/include/qt5/QtWebChannel/qtwebchannelversion.h
/usr/include/qt5/QtWebChannel/qwebchannel.h
/usr/include/qt5/QtWebChannel/qwebchannelabstracttransport.h
/usr/include/qt5/QtWebChannel/qwebchannelglobal.h
/usr/lib64/cmake/Qt5WebChannel/Qt5WebChannelConfig.cmake
/usr/lib64/cmake/Qt5WebChannel/Qt5WebChannelConfigVersion.cmake
/usr/lib64/libQt5WebChannel.prl
/usr/lib64/libQt5WebChannel.so
/usr/lib64/pkgconfig/Qt5WebChannel.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_webchannel.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_webchannel_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5WebChannel.so.5
/usr/lib64/libQt5WebChannel.so.5.14
/usr/lib64/libQt5WebChannel.so.5.14.0
/usr/lib64/qt5/qml/QtWebChannel/libdeclarative_webchannel.so
/usr/lib64/qt5/qml/QtWebChannel/plugins.qmltypes
/usr/lib64/qt5/qml/QtWebChannel/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtwebchannel/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qtwebchannel/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtwebchannel/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qtwebchannel/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtwebchannel/f45ee1c765646813b442ca58de72e20a64a7ddba
