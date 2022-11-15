%define debug_package %{nil}

Name:          libkysdk-system
Version:       1.0.0
Release:       1
Summary:       Kylin Software Development Kit - System Layer Kit
License:       GPL-2+
URL:           http://www.ukui.org
Source0:       %{name}-%{version}.tar.gz
Patch01:       0001-fix-compile-error-of-libkysdk-system.patch

BuildRequires: cmake
BuildRequires: glibc-devel
BuildRequires: systemd-devel
BuildRequires: dbus-devel
BuildRequires: dbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: libkysdk-log-devel
BuildRequires: libkysdk-config-devel
BuildRequires: libkysdk-utils-devel
BuildRequires: libkysdk-timer-devel
#compile need  but control is not exist
BuildRequires: gcc-c++


Requires: libkysdk-disk libkysdk-sysinfo libkysdk-systime

%description
Kylin Software Development Kit - System Layer Kit
Provides APIs and services such as system information, disk information, and system time


%package -n libkysdk-system-devel
Summary:  utils
Requires: libkysdk-system, libkysdk-disk-devel, libkysdk-sysinfo-devel, libkysdk-systime-devel, libkysdk-sysinfo-devel
 
%description -n libkysdk-system-devel
libkysdk-system Development libraries, Provides APIs and services such as system information, disk information, and system time


%package -n libkysdk-disk
Summary:  utils
Requires: libkysdk-log

%description -n libkysdk-disk
System disk information acquisition library


%package -n libkysdk-disk-devel
Summary:  utils
Requires: libkysdk-disk, libkysdk-log-devel, libkysdk-utils-devel, libudev-devel

%description -n libkysdk-disk-devel
System disk information acquisition library - Development libraries


%package -n libkysdk-systime
Summary:  utils
Requires: libkysdk-log, dbus, systemd, libkysdk-timer

%description -n libkysdk-systime
Library of system time-related operations


%package -n libkysdk-systime-devel
Summary:  utils
Requires: libkysdk-systime, libkysdk-timer-devel

%description -n libkysdk-systime-devel
Library of system time-related operations - Development libraries


%package -n libkysdk-sysinfo
Summary:  utils
Requires: libkysdk-log

%description -n libkysdk-sysinfo
System Information Acquisition Library


%package -n libkysdk-sysinfo-devel
Summary:  utils
Requires: libkysdk-sysinfo, libkysdk-log-devel, libkysdk-utils-devel

%description -n libkysdk-sysinfo-devel
System Information Acquisition Library - Development libraries

%prep
%setup -q
%patch01 -p1

%build
pushd build
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
systemctl daemon-reload
systemctl enable kysdk-systime.service
systemctl restart kysdk-systime.service

%files 

%files -n libkysdk-system-devel

%files -n libkysdk-disk
%{_prefix}/lib/kysdk/kysdk-system/libkydiskinfo.so

%files -n libkysdk-disk-devel
%{_includedir}/kysdk/kysdk-system/libkydiskinfo.h

%files -n libkysdk-systime
%{_bindir}/systime
%{_sysconfdir}/dbus-1/system.d/com.kylin.kysdk.TimeServer.conf
/lib/systemd/system/kysdk-systime.service

%files -n libkysdk-systime-devel
%{_includedir}/kysdk/kysdk-system/m_systime.h

%files -n libkysdk-sysinfo
%{_prefix}/lib/kysdk/kysdk-system/libkysysinfo.so

%files -n libkysdk-sysinfo-devel
%{_includedir}/kysdk/kysdk-system/libkysysinfo.hpp

%changelog
* Thu Nov 3 2022 peijiankang <peijiankang@kylinos.cn> - 1.0.0-1
- Init Package for libkysdk-system
