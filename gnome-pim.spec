Summary:	GNOME Personal Information Manager
Summary(pl):	Osobisty terminarz i mened¿er harmonogramów
Name:		gnome-pim
Version:	1.4.0
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-pim/%{name}-%{version}.tar.gz
Patch0:		%{name}-fontset.patch
Patch1:		%{name}-gettext.patch
Patch2:		%{name}-macros.patch
Icon:		gnome-pim.xpm
URL:		http://www.gnome.org/
Requires:	gnome-libs => 1.0.5
Requires:	ORBit => 0.4.0
Requires:	gtk+ >= 1.2.1
Requires:	glib >= 1.2.1
BuildRequires:	gnome-libs-devel
BuildRequires:	pilot-link-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	ORBit-devel
BuildRequires:	libstdc++-devel
BuildRequires:	flex
BuildRequires:	docbook-style-dsssl
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
Obsoletes:	gnome-pim-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
The GNOME Personal Information Manager consists of applications to
make keeping up with your busy life easier. Currently these apps are
present:
- gnomecal - personal calendar and todo list
- gnomecard - contact list of friends and business associates

%description -l pl
Pakiet zawiera aplikacje robi±ce Twoje zapracowane ¿ycie prostrzym.
Aktualnie dwie aplikacje s± obecne:
- gnomecal - prywatny terminarz i lista zadañ
- gnomecard - notatnik z kontaktami przyjació³ oraz partnerów
  biznesowych

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
gettextize --copy --force
libtoolize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-nls \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_applnkdir}/Office/PIMs

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%config %{_sysconfdir}/CORBA/servers/*

%attr(755,root,root) %{_bindir}/*

%{_applnkdir}/Office/PIMs/*
%{_datadir}/gnome/help/*
%{_datadir}/mime-info/gnome-pim.keys
%{_datadir}/idl/*
%{_pixmapsdir}/*
