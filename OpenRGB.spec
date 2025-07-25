%undefine _debugsource_packages

Name:           OpenRGB
Version:        0.9
Release:        2
Summary:        Open source RGB lighting control that doesn't depend on manufacturer software.
License:        GPLv2
URL:            https://gitlab.com/CalcProgrammer1/OpenRGB
Source0:        https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_%{version}/%{name}-release_%{version}.tar.bz2
Patch:		openrgb-0.9-qt6.patch

BuildRequires:  qmake-qt6
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

Provides:       openrgb

%description
The purpose of this tool is to control RGB lights on different peripherals.
Accessing the SMBus is a potentially dangerous operation, so exercise caution.

%prep
%autosetup -p1 -n %{name}-release_%{version}

%conf
%{_qtdir}/bin/qmake OpenRGB.pro

%build
%make_build

./scripts/build-udev-rules.sh $(pwd)

%install
install -Dpm0755 openrgb %{buildroot}/%{_bindir}/openrgb
install -Dpm0644 qt/OpenRGB.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dpm0644 60-openrgb.rules %{buildroot}%{_udevrulesdir}/60-openrgb.rules
install -Dpm0644 qt/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_bindir}/openrgb
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_udevrulesdir}/60-openrgb.rules
