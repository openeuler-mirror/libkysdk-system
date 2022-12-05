%define debug_package %{nil}

Name:          libkysdk-system
Version:       2.0.0
Release:       1
Summary:       Kylin Software Development Kit - System Layer Kit
License:       GPL-2+
URL:           http://www.ukui.org
Source0:       %{name}-%{version}.tar.gz
Patch01:       0001-fix-compile-error-of-libkysdk-system.patch

BuildRequires: cmake
BuildRequires: glibc-devel
BuildRequires: systemd-devel
BuildRequires: cjson-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: libkysdk-log-devel
BuildRequires: libkysdk-config-devel
BuildRequires: libkysdk-utils-devel
BuildRequires: libkysdk-timer-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: opencv
BuildRequires: libarchive-devel
BuildRequires: tesseract-devel
BuildRequires: cups-devel
BuildRequires: libcurl-devel
BuildRequires: libXrandr-devel


Requires: libkysdk-disk libkysdk-sysinfo libkysdk-systime libkysdk-filesystem libkysdk-proc libkysdk-hardware libkysdk-package libkysdk-powermanagement systemd glib2 libkysdk-systemcommon libkysdk-location libkysdk-net libkysdk-realtime

%description
Kylin Software Development Kit - System Layer Kit
Provides APIs and services such as system information, disk information, and system time


%package -n libkysdk-system-devel
Summary:  libkysdk-system Development libraries, Provides APIs and services such as system information, disk information, and system time
Requires: libkysdk-system libkysdk-disk-devel libkysdk-sysinfo-devel libkysdk-systime-devel libkysdk-filesystem-devel libkysdk-proc-devel libkysdk-hardware-devel libkysdk-package-devel libkysdk-powermanagement-devel libkysdk-location-devel libkysdk-net-devel libkysdk-realtime-devel
 
%description -n libkysdk-system-devel
%{summary}.


%package -n libkysdk-disk
Summary:  System disk information acquisition library
Requires: libkysdk-log libkysdk-systemcommon

%description -n libkysdk-disk
%{summary}.


%package -n libkysdk-disk-devel
Summary:  System disk information acquisition library - Development libraries
Requires: libkysdk-disk libkysdk-log-devel libkysdk-utils-devel util-linux-devel systemd-devel

%description -n libkysdk-disk-devel
%{summary}.


%package -n libkysdk-systime
Summary:  Library of system time-related operations
Requires: libkysdk-log dbus systemd libkysdk-timer glib2 libkysdk-timer libkysdk-systemcommon

%description -n libkysdk-systime
%{summary}.


%package -n libkysdk-systime-devel
Summary:  Library of system time-related operations - Development libraries
Requires: libkysdk-systime glib2-devel libkysdk-timer-devel

%description -n libkysdk-systime-devel
%{summary}.


%package -n libkysdk-sysinfo
Summary:  System Information Acquisition Library
Requires: libkysdk-log dbus glib2 systemd cjson libXrandr libkysdk-systemcommon

%description -n libkysdk-sysinfo
%{summary}.


%package -n libkysdk-sysinfo-devel
Summary:  System Information Acquisition Library - Development libraries
Requires: libkysdk-sysinfo libkysdk-log-devel libkysdk-utils-devel systemd-devel cjson-devel dbus-devel dbus-glib-devel glib2-devel libXrandr-devel

%description -n libkysdk-sysinfo-devel
%{summary}.


%package -n libkysdk-filesystem
Summary:  File System Library
Requires: libkysdk-log qt5-qtbase libkysdk-config systemd libkysdk-systemcommon

%description -n libkysdk-filesystem
%{summary}.


%package -n libkysdk-filesystem-devel
Summary:  File System Library - Development libraries
Requires: libkysdk-filesystem libkysdk-log-devel libkysdk-config-devel systemd-devel qt5-qtbase-devel

%description -n libkysdk-filesystem-devel
%{summary}.


%package -n libkysdk-hardware
Summary:  Hardware information acquisition library
Requires: libkysdk-log libkysdk-config systemd libkysdk-systemcommon cups-libs libcurl systemd

%description -n libkysdk-hardware
%{summary}.


%package -n libkysdk-hardware-devel
Summary:  Hardware information acquisition library - Development libraries
Requires: libkysdk-hardware libkysdk-log-devel libkysdk-config-devel systemd-devel cups-devel libcurl-devel systemd-devel

%description -n libkysdk-hardware-devel
%{summary}.


%package -n libkysdk-package
Summary:  Package Management Library
Requires: libkysdk-systemcommon

%description -n libkysdk-package
%{summary}.


%package -n libkysdk-package-devel
Summary:  Package Management Library - Development libraries
Requires: libkysdk-package

%description -n libkysdk-package-devel
%{summary}.


%package -n libkysdk-proc
Summary:  Runtime information retrieval library
Requires: libkysdk-systemcommon

%description -n libkysdk-proc
%{summary}.


%package -n libkysdk-proc-devel
Summary:  Runtime information retrieval library - Development libraries
Requires: libkysdk-proc

%description -n libkysdk-proc-devel
%{summary}.


%package -n libkysdk-powermanagement
Summary:  Power management library
Requires: libkysdk-log libkysdk-systemcommon

%description -n libkysdk-powermanagement
%{summary}.


%package -n libkysdk-powermanagement-devel
Summary:  Power management library - Development libraries
Requires: libkysdk-log-devel libkysdk-powermanagement

%description -n libkysdk-powermanagement-devel
%{summary}.


%package -n libkysdk-ocr
Summary:  AI character recognition function
Requires: opencv leptonica libarchive tesseract libkysdk-systemcommon

%description -n libkysdk-ocr
%{summary}.


%package -n libkysdk-ocr-devel
Summary:  AI character recognition function - Development libraries
Requires: libkysdk-ocr leptonica-devel libopencv-devel libarchive-devel tesseract-devel

%description -n libkysdk-ocr-devel
%{summary}.


%package -n libkysdk-systemcommon
Summary:  Kysdk system layer common data package

%description -n libkysdk-systemcommon
%{summary}.


%package -n libkysdk-location
Summary:  Geographic Location Library
Requires: libkysdk-systemcommon glib2

%description -n libkysdk-location
%{summary}.


%package -n libkysdk-location-devel
Summary:  Geographic Location Library - Development libraries
Requires: libkysdk-location

%description -n libkysdk-location-devel
%{summary}.


%package -n libkysdk-net
Summary:  Network information base
Requires: libkysdk-systemcommon

%description -n libkysdk-net
%{summary}.


%package -n libkysdk-net-devel
Summary:  Network information base - Development libraries
Requires: libkysdk-net

%description -n libkysdk-net-devel
%{summary}.


%package -n libkysdk-realtime
Summary:  Runtime repository
Requires: libkysdk-systemcommon

%description -n libkysdk-realtime
%{summary}.


%package -n libkysdk-realtime-devel
Summary:  Runtime repository - Development libraries
Requires: libkysdk-realtime

%description -n libkysdk-realtime-devel
%{summary}.


%prep
%setup -q
%patch01 -p1

%build
mkdir build && pushd build
cmake ..
make -j4
popd

%install
rm -rf $RPM_BUILD_ROOT 
pushd build
make DESTDIR=%{buildroot} install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post
check_env=`systemd-detect-virt`
echo $check_env
if [ $check_env = "docker" ];then
    echo "docker env do not start kysdk-systime.service"
else
    systemctl daemon-reload
    systemctl enable kysdk-systime.service
    systemctl restart kysdk-systime.service
fi

if [ -f "/usr/lib/libpaddle_inference.so/libpaddle_inference" ]
then
        rm -rf /usr/lib/libpaddle_inference.so/
fi


%files 

%files -n libkysdk-system-devel
%{_datadir}/kgconfig/kysdk-system.pc

%files -n libkysdk-disk
%{_prefix}/lib/kysdk/kysdk-system/libkydiskinfo.so*

%files -n libkysdk-disk-devel
%{_includedir}/kysdk/kysdk-system/libkydiskinfo.h
%{_datadir}/kgconfig/kysdk-disk.pc

%files -n libkysdk-systime
%{_bindir}/systime
%{_sysconfdir}/dbus-1/system.d/com.kylin.kysdk.TimeServer.conf
/lib/systemd/system/kysdk-systime.service

%files -n libkysdk-systime-devel
%{_includedir}/kysdk/kysdk-system/m_systime.h

%files -n libkysdk-sysinfo
%{_prefix}/lib/kysdk/kysdk-system/libkysysinfo.so*

%files -n libkysdk-sysinfo-devel
%{_includedir}/kysdk/kysdk-system/libkysysinfo.hpp
%{_includedir}/kysdk/kysdk-system/libkysysinfo.h
%{_datadir}/kgconfig/kysdk-sysinfo.pc

%files -n libkysdk-filesystem
%{_prefix}/lib/kysdk/kysdk-system/libkyfilewatcher.so*

%files -n libkysdk-filesystem-devel
%{_includedir}/kysdk/kysdk-system/libkyfilewatcher.hpp
%{_includedir}/kysdk/kysdk-system/libkyfilewatcher_global.hpp
%{_datadir}/kgconfig/kysdk-filesystem.pc

%files -n libkysdk-hardware
%{_prefix}/lib/kysdk/kysdk-system/libkyhw.so*

%files -n libkysdk-hardware-devel
%{_includedir}/kysdk/kysdk-system/libkync.h
%{_includedir}/kysdk/kysdk-system/libkycpu.h
%{_includedir}/kysdk/kysdk-system/libkyprinter.h
%{_includedir}/kysdk/kysdk-system/libkybios.h
%{_includedir}/kysdk/kysdk-system/libkyboard.h
%{_includedir}/kysdk/kysdk-system/libkyusb.h
%{_datadir}/kgconfig/kysdk-hardware.pc

%files -n libkysdk-package
%{_prefix}/lib/kysdk/kysdk-system/libkypackage.so*

%files -n libkysdk-package-devel
%{_includedir}/kysdk/kysdk-system/libkypackages.h
%{_datadir}/kgconfig/kysdk-package.pc

%files -n libkysdk-proc
%{_prefix}/lib/kysdk/kysdk-system/libkyrtinfo.so*

%files -n libkysdk-proc-devel
%{_includedir}/kysdk/kysdk-system/libkyrtinfo.h
%{_includedir}/kysdk/kysdk-system/libkyprocess.h
%{_datadir}/kgconfig/kysdk-proc.pc

%files -n libkysdk-powermanagement
%{_prefix}/lib/kysdk/kysdk-system/libkypowermanagement.so*

%files -n libkysdk-powermanagement-devel
%{_includedir}/kysdk/kysdk-system/libkylockscreen.h
%{_datadir}/kgconfig/kysdk-powermanagement.pc

%files -n libkysdk-ocr
%{_prefix}/lib/kysdk/kysdk-system/libkyocr.so*
%{_prefix}/lib/libpaddle_inference.so
%{_sysconfdir}/kdkocr/*

%files -n libkysdk-ocr-devel
%{_includedir}/kysdk/kysdk-system/libkyocr.hpp
%{_datadir}/kgconfig/kysdk-ocr.pc

%files -n libkysdk-systemcommon
%{_sysconfdir}/ld.so.conf.d/kysdk-system.conf

%files -n libkysdk-location
%{_prefix}/lib/kysdk/kysdk-system/libkylocation.so*
%{_bindir}/location.py
%{_sysconfdir}/dbus-1/system.d/dbus_location.conf
/lib/systemd/system/dbus_location.service

%files -n libkysdk-location-devel
%{_includedir}/kysdk/kysdk-system/libkylocation.h
%{_datadir}/kgconfig/kysdk-location.pc

%files -n libkysdk-net
%{_prefix}/lib/kysdk/kysdk-system/libkynetinfo.so*

%files -n libkysdk-net-devel
%{_includedir}/kysdk/kysdk-system/libkynetinfo.h
%{_datadir}/kgconfig/kysdk-net.pc

%files -n libkysdk-realtime
%{_prefix}/lib/kysdk/kysdk-system/libkyrealtime.so*

%files -n libkysdk-realtime-devel
%{_includedir}/kysdk/kysdk-system/libkyrealtimeinfo.h
%{_datadir}/kgconfig/kysdk-realtime.pc


%changelog
* Mon Dec 5 2022 peijiankang <peijiankang@kylinos.cn> - 2.0.0-1
- update version to 2.0.0

* Thu Nov 3 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.0-1
- Init Package for libkysdk-system
