Summary:	Graphical frontend for git
Summary(pl.UTF-8):	Graficzna nakładka na git
Name:		giggle
Version:	0.4
Release:	1
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://ftp.imendio.com/pub/imendio/giggle/src/%{name}-%{version}.tar.gz
# Source0-md5:	695b381d42de8338626068dfa5341406
URL:		http://developer.imendio.com/projects/giggle
Patch0:		%{name}-pl.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	git-core >= 1.4.4.3
BuildRequires:	glib2-devel >= 1:2.12
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	gtksourceview2-devel >= 2.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	desktop-file-utils
Requires:	git-core >= 1.4.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Giggle is a GTK+ based GIT repositories viewer, providing developers a
way to browse and visualize graphically revision trees, change logs,
diffs, and other useful information.

%description -l pl.UTF-8
Giggle jest bazującą na GTK+ przeglądarką repozytoriów GIT, dającą
deweloperom możliwość przeglądania i wizualizacji drzew rewizji, list
zmian, różnić i innych przydatnych informacji.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
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
%{_datadir}/%{name}
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/*
%{_libdir}/libgiggle-0.4.so
