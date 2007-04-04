Summary:	Graphical frontend for git
Summary(pl.UTF-8):	Graficzna nakładka na git
Name:		giggle
Version:	0.2
Release:	2
License:	GPL v2
Group:		X11/Development/Tools
Source0:	http://ftp.imendio.com/pub/imendio/giggle/src/%{name}-%{version}.tar.gz
# Source0-md5:	ef23f4c4d3d30a9338b95437828a7e03
URL:		http://developer.imendio.com/projects/giggle
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	git-core >= 1.4.4.3
BuildRequires:	glib2-devel >= 1:2.12
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	gtksourceview-devel >= 1.8
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel >= 1:2.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	desktop-file-utils
Requires:	git-core >= 1.4.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Giggle is a graphical frontend for the git directory tracker.

%description -l pl.UTF-8
Giggle jest graficzną nakładką na git.

%prep
%setup -q

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
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
