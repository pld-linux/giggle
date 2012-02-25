#
# TODO:
#	- seperate out libgiggle/libgiggle-git
#
Summary:	Graphical frontend for git
Summary(pl.UTF-8):	Graficzna nakładka na git
Name:		giggle
Version:	0.6.1
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/giggle/0.6/%{name}-%{version}.tar.xz
# Source0-md5:	dd80ffa12f10a1c687bd3e730a14ca8b
URL:		http://live.gnome.org/giggle
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1.11
BuildRequires:	evolution-data-server-devel
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	git-core >= 1.4.4.3
BuildRequires:	glib2-devel >= 1:2.18
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtksourceview3-devel >= 3.0.0
BuildRequires:	intltool >= 0.41.0
BuildRequires:	itstool
BuildRequires:	libtool >= 2.2.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	vte-devel >= 0.26
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	git-core >= 1.4.4.3
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
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/giggle/plugins/*/*.la \
	$RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome

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
%attr(755,root,root) %{_bindir}/giggle
%attr(755,root,root) %{_libdir}/libgiggle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiggle.so.0
%attr(755,root,root) %{_libdir}/libgiggle-git.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgiggle-git.so.0
%dir %{_libdir}/giggle
%dir %{_libdir}/giggle/plugins
%dir %{_libdir}/giggle/plugins/%{version}
%attr(755,root,root) %{_libdir}/giggle/plugins/%{version}/libpersonal-details.so
%attr(755,root,root) %{_libdir}/giggle/plugins/%{version}/libterminal-view.so
%{_libdir}/giggle/plugins/%{version}/personal-details.xml
%{_libdir}/giggle/plugins/%{version}/terminal-view.xml
%{_datadir}/%{name}
%{_desktopdir}/giggle.desktop
%{_iconsdir}/hicolor/*/*/*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/giggle
%{_includedir}/giggle/libgiggle
%{_includedir}/giggle/libgiggle-git
%{_libdir}/libgiggle.so
%{_libdir}/libgiggle-git.so
