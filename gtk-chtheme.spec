Name:		gtk-chtheme
Version:	0.3.1
Release:	%mkrel 7
Summary:	Utility to preview and change GTK 2 themes
Source:		%{name}-%{version}.tar.bz2
Source1:	gtk.png
Patch1:		gtk-chtheme-0.3.1-fix-build-with-gtk.patch
Patch2:		gtk-chtheme-0.3.1-dont-strip-binary-too-early.patch
URL:		http://plasmasturm.org/programs/gtk-chtheme/
Group:		Graphical desktop/GNOME
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libgtk+2-devel
BuildRequires:	imagemagick

%description
Gtk-chtheme allows you to change the Gtk+ 2.0 theme when not using GNOME.

%prep
%setup -q
%patch1 -p1 -b .gtk
%patch2 -p1 -b .strip

%build
%setup_compile_flags
%make PREFIX=%{_prefix}

%install
rm -rf %{buildroot}
%makeinstall_std

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Change GTK-2.0 theme
Exec=%{name} 
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
%doc ChangeLog COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.*
