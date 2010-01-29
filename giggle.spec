#
# TODO:
#	- seperate out libgiggle/libgiggle-git
#
Summary:	Graphical frontend for git
Summary(pl.UTF-8):	Graficzna nakładka na git
Name:		giggle
Version:	0.4.95
Release:	2
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/giggle/0.4/%{name}-%{version}.tar.gz
# Source0-md5:	b8c385971bcfcd35202fb6f02a79350f
URL:		http://live.gnome.org/giggle
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	git-core >= 1.4.4.3
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	gtk+2-devel >= 2:2.18
BuildRequires:	gtksourceview2-devel >= 2.8
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vte-devel >= 0.17
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	git-core >= 1.4.4.3
Requires:	gtk+2 >= 2:2.10
Requires:	libglade2 >= 1:2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Giggle is a GTK+ based GIT repositories viewer, providing developers a
way to browse and visualize graphically revision trees, change logs,
diffs, and other useful information.

%description -l pl.UTF-8
Giggle jest opartą na GTK+ przeglądarką repozytoriów GIT, dającą
deweloperom możliwość przeglądania i wizualizacji drzew rewizji, list
zmian, różnic i innych przydatnych informacji.

%package devel
Summary:	libgiggle development files
Summary(pl.UTF-8):	Pliki programistyczne libgiggle
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libgiggle development files.

%description devel -l pl.UTF-8
Pliki programistyczne libgiggle.


%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libgiggle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiggle.so.0
%attr(755,root,root) %{_libdir}/libgiggle-git.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiggle-git.so.0
%dir %{_libdir}/giggle
%dir %{_libdir}/giggle/plugins
%dir %{_libdir}/giggle/plugins/%{version}
%attr(755,root,root) %{_libdir}/giggle/plugins/%{version}/libpersonal-details.so
%attr(755,root,root) %{_libdir}/giggle/plugins/%{version}/libterminal-view.so
%{_libdir}/giggle/plugins/%{version}/*.xml
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/giggle
%dir %{_includedir}/giggle/libgiggle
%{_includedir}/giggle/libgiggle/*.h
%dir %{_includedir}/giggle/libgiggle-git
%{_includedir}/giggle/libgiggle-git/*.h
%{_libdir}/*.la
%ghost %{_libdir}/*.so
