Summary: Utility to preview and change GTK 2 themes
Name:    gtk-chtheme
Version: 0.3.1
Release: %mkrel 1
Source:  %name-%version.tar.bz2
URL:     http://plasmasturm.org/programs/gtk-chtheme/
Group:   Graphical desktop/GNOME
License: GPL
BuildRoot: %_tmppath/%name-%version-build
BuildRequires: libgtk+2-devel

%description
Gtk-chtheme enable to change the Gtk+ 2.0 theme.

%prep
%setup -q

%build
export CFLAGS=$RPM_OPT_FLAGS
%make PREFIX=%_prefix

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
install -s -m 755 gtk-chtheme $RPM_BUILD_ROOT%_bindir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%_bindir/*
