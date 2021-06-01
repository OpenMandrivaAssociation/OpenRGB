Name:           OpenRGB
Version:        0.6
Release:        1
Summary:        Open source RGB lighting control that doesn't depend on manufacturer software.
License:        GPLv2
URL:            https://gitlab.com/CalcProgrammer1/OpenRGB
Source0:        https://gitlab.com/CalcProgrammer1/OpenRGB/-/archive/release_%{version}/%{name}-release_%{version}.tar.bz2

BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gusb)
BuildRequires:  pkgconfig(hidapi-hidraw)

%description
The purpose of this tool is to control RGB lights on different peripherals.
Accessing the SMBus is a potentially dangerous operation, so exercise caution.

%prep
%autosetup -p1 -n %{name}-release_%{version}

%build
%qmake_qt5
%make_build

%install
install -Dpm0755 openrgb %{buildroot}/%{_bindir}/openrgb
install -Dpm0644 qt/OpenRGB.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dpm0644 60-openrgb.rules %{buildroot}%{_udevrulesdir}/60-openrgb.rules

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
