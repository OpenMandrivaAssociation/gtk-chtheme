Name:		gtk-chtheme
Version:	0.3.1
Release:	9
Summary:	Utility to preview and change GTK 2 themes
Source0:		%{name}-%{version}.tar.bz2
Source1:	gtk.png
Patch1:		gtk-chtheme-0.3.1-fix-build-with-gtk.patch
Patch2:		gtk-chtheme-0.3.1-dont-strip-binary-too-early.patch
Patch3:		gtk-chtheme-0.3.1-replace_deprecated_GtkFunction.patch
Patch4:		gtk-chtheme-0.3.1-fix_linking.patch
URL:		https://plasmasturm.org/programs/gtk-chtheme/
Group:		Graphical desktop/GNOME
License:	GPLv2
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	imagemagick

%description
Gtk-chtheme allows you to change the Gtk+ 2.0 theme when not using GNOME.

%prep
%setup -q
%patch1 -p1 -b .gtk
%patch2 -p1 -b .strip
%patch3 -p0 -b .GtkFunction
%patch4 -p0 -b .linking

%build
%setup_compile_flags
%make PREFIX=%{_prefix} LDFLAGS="%{ldflags}"

%install
%makeinstall_std

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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


%changelog
* Wed Apr 27 2011 Jani Välimaa <wally@mandriva.org> 0.3.1-8mdv2011.0
+ Revision: 659742
- add patch to fix build with Gtk >2.24
- add patch to fix overlinking
- use _real_vendor macro in desktop file name
- drop buildroot definition

* Fri Oct 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.1-7mdv2011.0
+ Revision: 587216
- Add patch to make it build with latest gtk (Fedora)
- Add patch to not strip the binary too early in order to have a useful debug
  package
- Clean spec and fix license tag

* Sun Jan 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.3.1-6mdv2010.1
+ Revision: 488309
- fix icon sizes (bug 56932)
- clean spec

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3.1-5mdv2010.0
+ Revision: 429334
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3.1-4mdv2009.0
+ Revision: 246678
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3.1-2mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Jun 07 2007 Austin Acton <austin@mandriva.org> 0.3.1-2mdv2008.0
+ Revision: 36597
- add menu entry and icons
- fix description

* Tue Apr 24 2007 Thierry Vignaud <tv@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 17857
- new release
- Import gtk-chtheme



* Fri Nov 05 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.2-2mdk
- add BuildRequires: libgtk+2-devel

* Fri Jan 30 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2-1mdk
- initial release
