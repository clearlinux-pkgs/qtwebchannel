#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtwebchannel
Version  : 5.10.1
Release  : 2
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtwebchannel-everywhere-src-5.10.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtwebchannel-everywhere-src-5.10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtwebchannel-lib
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Quick)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5WebSockets)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev

%description
A REPL client for any qwebchannel service using a websocket transport.
A nice tool for testing qwebchannel endpoints.

%package dev
Summary: dev components for the qtwebchannel package.
Group: Development
Requires: qtwebchannel-lib
Provides: qtwebchannel-devel

%description dev
dev components for the qtwebchannel package.


%package lib
Summary: lib components for the qtwebchannel package.
Group: Libraries

%description lib
lib components for the qtwebchannel package.


%prep
%setup -q -n qtwebchannel-everywhere-src-5.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtWebChannel/5.10.1/QtWebChannel/private/qmetaobjectpublisher_p.h
/usr/include/qt5/QtWebChannel/5.10.1/QtWebChannel/private/qqmlwebchannelattached_p.h
/usr/include/qt5/QtWebChannel/5.10.1/QtWebChannel/private/qwebchannel_p.h
/usr/include/qt5/QtWebChannel/5.10.1/QtWebChannel/private/signalhandler_p.h
/usr/include/qt5/QtWebChannel/5.10.1/QtWebChannel/private/variantargument_p.h
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
/usr/lib64/libQt5WebChannel.la
/usr/lib64/libQt5WebChannel.prl
/usr/lib64/libQt5WebChannel.so
/usr/lib64/pkgconfig/Qt5WebChannel.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_webchannel.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_webchannel_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5WebChannel.so.5
/usr/lib64/libQt5WebChannel.so.5.10
/usr/lib64/libQt5WebChannel.so.5.10.1
/usr/lib64/qt5/qml/QtWebChannel/libdeclarative_webchannel.so
/usr/lib64/qt5/qml/QtWebChannel/plugins.qmltypes
/usr/lib64/qt5/qml/QtWebChannel/qmldir
