# TODO:
#  - fix gnomecal conduit - libcalendar_conduit (linking problem ?)
#  - fix conduits i18n (proper gettext domain binding)
#
%bcond_without	pilot_support

Summary:	GNOME Personal Information Manager
Summary(es):	El administrador de informaciones personales del GNOME
Summary(ja):	The GNOME ¸Ä¿Í¾ðÊó´ÉÍý¥Þ¥Í¡¼¥¸¥ã
Summary(pl):	Osobisty terminarz i mened¿er harmonogramów
Summary(pt_BR):	O gerenciador de informações pessoais do GNOME
Summary(ru):	ðÅÒÓÏÎÁÌØÎÙÊ ÉÎÆÏÒÍÁÃÉÏÎÎÙÊ ÍÅÎÅÄÖÅÒ (PIM) ÄÌÑ GNOME
Summary(uk):	ðÅÒÓÏÎÁÌØÎÉÊ ¦ÎÆÏÒÍÁÃ¦ÊÎÉÊ ÍÅÎÅÄÖÅÒ (PIM) ÄÌÑ GNOME
Summary(zh_CN):	GNOME¸öÈËÐÅÏ¢¹ÜÀí¹¤¾ß
Name:		gnome-pim
Version:	1.4.9
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://www.jroger.in-berlin.de/gnome-pim//%{name}-%{version}.tar.gz
# Source0-md5:	849babfa25e08eb7616d20e826f7fb6d
Patch0:		%{name}-pl.patch
Patch1:		%{name}-gettext.patch
Patch2:		%{name}-macros.patch
Patch3:		%{name}-lt.patch
Patch4:		%{name}-am.patch
Patch5:		%{name}-desktop.patch
Icon:		gnome-pim.xpm
URL:		http://www.gnome.org/
Requires:	gnome-libs => 1.0.5
Requires:	ORBit => 0.4.0
Requires:	gtk+ >= 1.2.1
Requires:	glib >= 1.2.1
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-style-dsssl
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
%{?with_pilot_support:BuildRequires:	gnome-pilot-devel}
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	pilot-link-devel
Obsoletes:	gnome-pim-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
The GNOME Personal Information Manager consists of applications to
make keeping up with your busy life easier. Currently these apps are
present:
- gnomecal : personal calendar and todo list,
- gnomecard: contact list of friends and business associates.

%description -l es
El administrador de informaciones personales del GNOME consiste de
aplicaciones para hacer su vida muy mas fácil. Actualmente estas
aplicaciones están presentes:
- gnomecal : calendario personal,
- gnomecard: lista de contactos.

%description -l ja
GNOME ¸Ä¿Í¾ðÊó´ÉÍý¥Þ¥Í¡¼¥¸¥ã¤Ë¤Ï¡¢Ë»¤·¤¤ËèÆü¤ò¤Á¤ç¤Ã¤È³Ú¤Ë¤·¤Æ¤¯¤ì
¤ë¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤¬´Þ¤Þ¤ì¤Æ¤¤¤Þ¤¹¡£
¸½ºß¡¢°Ê²¼¤Î¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤¬»È¤¨¤Þ¤¹:
- gnomecal : ¥Ñ¡¼¥½¥Ê¥ë¤Ê¥«¥ì¥ó¥À¡¼¤È To Do ¥ê¥¹¥È
- gnomecard: Í§¿Í¤ä¥Ó¥¸¥Í¥¹´Ø·¸¼Ô¤ÎÏ¢ÍíÀè¥ê¥¹¥È

%description -l pl
Pakiet zawiera aplikacje robi±ce Twoje zapracowane ¿ycie prostrzym.
Aktualnie dwie aplikacje s± obecne:
- gnomecal : prywatny terminarz i lista zadañ,
- gnomecard: notatnik z kontaktami przyjació³ oraz partnerów
  biznesowych.

%description -l pt_BR
O gerente de informações pessoais do GNOME consiste de aplicações para
manter sua vida mais fácil. Atualmente estes são os aplicativos
disponíveis:
- gnomecal : calendário pessoal e lista de coisas a fazer,
- gnomecard: lista de contatos: amigos e parceiros comerciais.

%description -l ru
ðÅÒÓÏÎÁÌØÎÙÊ ÉÎÆÏÒÍÁÃÉÏÎÎÙÊ ÍÅÎÅÄÖÅÒ ÓÏÓÔÏÉÔ ÉÚ ÐÒÉÌÏÖÅÎÉÊ,
ÏÂÌÅÇÞÁÀÝÉÈ ÖÉÚÎØ ÚÁÎÑÔÙÈ ÌÀÄÅÊ. ÷ ÎÁÓÔÏÑÝÅÅ ×ÒÅÍÑ ÜÔÏ ÓÌÅÄÕÀÝÉÅ
ÐÒÏÇÒÁÍÍÙ:
- gnomecal : ÐÅÒÓÏÎÁÌØÎÙÊ ËÁÌÅÎÄÁÒØ É ÓÐÉÓÏË ÄÅÌ (todo),
- gnomecard: ÓÐÉÓÏË ËÏÎÔÁËÔÏ×.

%description -l uk
ðÅÒÓÏÎÁÌØÎÉÊ ¦ÎÆÏÒÍÁÃ¦ÊÎÉÊ ÍÅÎÅÄÖÅÒ ÓËÌÁÄÁ¤ÔØÓÑ Ú ÐÒÉËÌÁÄÎÉÈ ÐÒÏÇÒÁÍ,
ÝÏ ÐÏÌÅÇÛÕÀÔØ ÖÉÔÔÑ ÚÁÊÎÑÔÉÈ ÌÀÄÅÊ. îÁÒÁÚ¦ ÃÅ ÎÁÓÔÕÐÎ¦ ÐÒÏÇÒÁÍÉ:
- gnomecal : ÐÅÒÓÏÎÁÌØÎÉÊ ËÁÌÅÎÄÁÒ ÔÁ ÓÐÉÓÏË ÓÐÒÁ× (todo),
- gnomecard: ÓÐÉÓÏË ËÏÎÔÁËÔ¦×.

%package conduits
Summary:	GNOME Pilot conduits for GnomeCal and GnomeCard
Summary(pl):	
Group:		Office
Requires:	%{name} = %{version}
Requires:	gnome-pilot >= 0.1.62

%description conduits
The gnome-pim-conduits package includes the conduits needed to connect
your PalmPilot with gnome-pim applications. Currently these conduits
are present:
- gnomecal : synchronizes your GnomeCal calendar with your Palm's
             calendar,
- gnomecard: synchronizes your contact list.

%description conduits -l pl
Pakiet gnome-pim-conduits zawiera ³±cza niezbêdne do komunikacji
PalmPilota z aplikacjami gnome-pim. Aktualnie dwa ³±cza s± obecne:
- gnomecal : do synchronizacji prywatny terminarz GnomeCala z
             kalendarzem Palm-Pilota,
- gnomecard: do synchronizacji listy kontaktów.

%prep
%setup  -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f missing
gettextize --copy --force
%{__libtoolize}
aclocal -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-nls \
	--without-included-gettext
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Productivitydir=%{_applnkdir}/Office/PIMs \
	productivitydir=%{_applnkdir}/Office/PIMs

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config %{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Office/PIMs/*
%{_datadir}/mime-info/gnome-pim.keys
%{_pixmapsdir}/gnome-gnomecard.png
%{_datadir}/idl/*

%if %{with pilot_support}
%files conduits
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnome-pilot/conduits/*.so*
%{_pixmapsdir}/gnome-calendar-conduit.png
%{_datadir}/gnome-pilot/conduits/*
%endif
