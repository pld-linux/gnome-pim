Summary:	GNOME Personal Information Manager
Name:		gnome-pim
Version:	1.0.8
Release:	1
Copyright:	GPL
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-pim/%{name}-%{version}.tar.gz
Patch:		gnome-pim-DESTDIR.patch
Icon:		gnome-pim.gif
URL:		http://www.gnome.org/
Requires:	gnome-libs => 1.0.5
Requires:	ORBit => 0.4.0
Requires:	gtk+ >= 1.2.1
Requires:	glib >= 1.2.1
BuildPrereq:	gnome-libs-devel
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	imlib-devel
BuildPrereq:	ORBit-devel
BuildPrereq:	XFree86-devel
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%define		_prefix /usr/X11R6
%define		_mandir /usr/X11R6/man

%description
The GNOME Personal Information Manager consists of applications to make
keeping up with your busy life easier.

Currently these apps are present:

 - gnomecal :  personal calendar and todo list
 - gnomecard:  contact list of friends and business associates

%package devel
Summary:	GNOME pim libraries, includes, etc
Group:		X11/GNOME/Development/Libraries
Group(pl):	X11/GNOME/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
GNOME pim libraries, includes, etc.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
autoconf
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--sysconfdir=/etc/X11/GNOME \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9fn AUTHORS ChangeLog NEWS README

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%config /etc/X11/GNOME/CORBA/servers/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/gnome/apps/Applications/*
%{_datadir}/gnome/help/*
%{_datadir}/mime-info/gnome-pim.keys
%{_datadir}/pixmaps/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_datadir}/idl/*
