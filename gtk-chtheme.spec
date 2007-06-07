Name:    gtk-chtheme
Version: 0.3.1
Release: %mkrel 2

Summary: Utility to preview and change GTK 2 themes
Source:  %name-%version.tar.bz2
Source1: gtk.png
URL:     http://plasmasturm.org/programs/gtk-chtheme/
Group:   Graphical desktop/GNOME
License: GPL
BuildRoot: %_tmppath/%name-%version-build
BuildRequires: libgtk+2-devel
BuildRequires: ImageMagick

%description
Gtk-chtheme allows you to change the Gtk+ 2.0 theme when not using GNOME.

%prep
%setup -q

%build
export CFLAGS=$RPM_OPT_FLAGS
%make PREFIX=%_prefix

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
install -s -m 755 gtk-chtheme $RPM_BUILD_ROOT%_bindir

# menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
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
cp %SOURCE1 %name.png
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 %name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 %name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 %name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

# FDo icons
mkdir -p %buildroot/%_iconsdir/hicolor/64x64/apps
convert -size 64x64 %name.png %buildroot/%_iconsdir/hicolor/64x64/apps/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/48x48/apps
convert -size 48x48 %name.png %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/32x32/apps
convert -size 32x32 %name.png %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
mkdir -p %buildroot/%_iconsdir/hicolor/16x16/apps
convert -size 16x16 %name.png %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog
%_bindir/%name
%{_datadir}/applications/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/hicolor/64x64/apps/%name.png
%{_iconsdir}/hicolor/48x48/apps/%name.png
%{_iconsdir}/hicolor/32x32/apps/%name.png
%{_iconsdir}/hicolor/16x16/apps/%name.png

