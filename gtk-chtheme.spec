Name:    gtk-chtheme
Version: 0.3.1
Release: %mkrel 6

Summary:	Utility to preview and change GTK 2 themes
Source:		%{name}-%{version}.tar.bz2
Source1:	gtk.png
URL:		http://plasmasturm.org/programs/gtk-chtheme/
Group:		Graphical desktop/GNOME
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libgtk+2-devel
BuildRequires:	imagemagick

%description
Gtk-chtheme allows you to change the Gtk+ 2.0 theme when not using GNOME.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make PREFIX=%{_prefix}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -s -m 755 gtk-chtheme %{buildroot}%{_bindir}

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Change GTK-2.0 theme
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=GTK;Utility;DesktopSettings;
EOF

# icons
cp %{SOURCE1} %{name}.png
mkdir -p %{buildroot}/%{_liconsdir}
convert %{name}.png -resize 48x48 %{buildroot}/%_liconsdir/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}
convert %{name}.png -resize 32x32 %{buildroot}/%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}/%{_miconsdir}
convert %{name}.png -resize 16x16 %{buildroot}/%{_miconsdir}/%{name}.png

# FDo icons
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/64x64/apps
convert %{name}.png -resize 64x64 %{buildroot}/%{_iconsdir}/hicolor/64x64/apps/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/48x48/apps
convert %{name}.png -resize 48x48 %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/32x32/apps
convert %{name}.png -resize 32x32 %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
mkdir -p %{buildroot}/%{_iconsdir}/hicolor/16x16/apps
convert %{name}.png -resize 16x16 %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png

