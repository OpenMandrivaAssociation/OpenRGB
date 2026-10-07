%undefine _debugsource_packages
%define oname openrgb

Name:           OpenRGB
Version:        1.0
Release:        1
Summary:        Open source RGB lighting control that doesn't depend on manufacturer software
License:        GPL-2.0-only
URL:            https://gitlab.com/CalcProgrammer1/OpenRGB
Source0:        https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_%{version}/%{name}-release_%{version}.tar.bz2

BuildRequires:  qmake-qt6
BuildRequires:  make
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  stdc++-devel
BuildRequires:  stdc++-static-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mbedtls-devel

Requires: python-smbus

Provides:       %{oname}

%description
The purpose of this tool is to control RGB lights on different peripherals.
Accessing the SMBus is a potentially dangerous operation, so exercise caution.

%prep
%autosetup -p1 -n %{name}-release_%{version}


%build
%{_bindir}/qmake-qt6 %{name}.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

# Generate the udev rules with the freshly installed OpenRGB binary.
%{buildroot}%{_bindir}/%{oname} --generate-udev-rules 60-%{oname}.rules
install -p -D --mode=0644 60-%{oname}.rules %{buildroot}%{_udevrulesdir}/60-%{oname}.rules

#desktop
desktop-file-install qt/org.%{oname}.%{name}.desktop

%post
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi

%files
%license LICENSE
%doc README.md Documentation
%{_bindir}/%{oname}
%{_datadir}/applications/org.%{oname}.%{name}.desktop
%{_datadir}/metainfo/org.%{oname}.%{name}.metainfo.xml
%{_iconsdir}/hicolor/128x128/apps/org.%{oname}.%{name}.png
%{_unitdir}/%{oname}.service
%{_tmpfilesdir}/openrgb.conf
%{_udevrulesdir}/60-%{oname}.rules
