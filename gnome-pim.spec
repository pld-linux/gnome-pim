Summary:	GNOME Personal Information Manager
Name:		gnome-pim
Version:	1.0.7
Release:	1
Copyright:	GPL
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/gnome-pim/%{name}-%{version}.tar.gz
Patch:		gnome-pim-DESTDIR.patch
Icon:		gnome-pim.gif
BuildPrereq:	gnome-libs-devel
BuildPrereq:	ORBit-devel
BuildPrereq:	gtk+-devel
BuildPrereq:	glib-devel
BuildPrereq:	XFree86-devel
URL:		http://www.gnome.org/
BuildRoot:	/tmp/%{name}-%{version}-root
Obsoletes:	gnome

%description
The GNOME Personal Information Manager consists of applications to make
keeping up with your busy life easier.

Currently these apps are present:

 - gnomecal :  personal calendar and todo list
 - gnomecard:  contact list of friends and business associates

%package devel
Summary:	GNOME pim libraries, includes, etc
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
GNOME pim libraries, includes, etc.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11/GNOME \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9fn AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz

%lang(de) /usr/X11R6/share/locale/de/LC_MESSAGES/gnome-pim.mo
%lang(es) /usr/X11R6/share/locale/es/LC_MESSAGES/gnome-pim.mo
%lang(fi) /usr/X11R6/share/locale/fi/LC_MESSAGES/gnome-pim.mo
%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/gnome-pim.mo
%lang(ga) /usr/X11R6/share/locale/ga/LC_MESSAGES/gnome-pim.mo
%lang(hu) /usr/X11R6/share/locale/hu/LC_MESSAGES/gnome-pim.mo
%lang(it) /usr/X11R6/share/locale/it/LC_MESSAGES/gnome-pim.mo
%lang(ja) /usr/X11R6/share/locale/ja/LC_MESSAGES/gnome-pim.mo
%lang(ko) /usr/X11R6/share/locale/ko/LC_MESSAGES/gnome-pim.mo
%lang(no) /usr/X11R6/share/locale/no/LC_MESSAGES/gnome-pim.mo
%lang(pt) /usr/X11R6/share/locale/pt/LC_MESSAGES/gnome-pim.mo
%lang(ru) /usr/X11R6/share/locale/ru/LC_MESSAGES/gnome-pim.mo
%lang(sv) /usr/X11R6/share/locale/sv/LC_MESSAGES/gnome-pim.mo

%config /etc/X11/GNOME/CORBA/servers/*

%attr(755, root, root) /usr/X11R6/bin/*

/usr/X11R6/share/gnome/apps/Applications/*
/usr/X11R6/share/gnome/help/*
/usr/X11R6/share/mime-info/gnome-pim.keys
/usr/X11R6/share/pixmaps/*


%files devel
%defattr(644, root, root, 755)
/usr/X11R6/lib/lib*.a
/usr/X11R6/share/idl/*

%changelog
* Fri Apr  9 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0.7-1]
- first version in rpm package for PLD.
