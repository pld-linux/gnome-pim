Summary:	GNOME Personal Information Manager
Summary(es): El administrador de informaciones personales del GNOME
Summary(pl):	Osobisty terminarz i mened¿er harmonogramów
Summary(pt_BR): O gerenciador de informações pessoais do GNOME
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
Patch3:		%{name}-gnomecal.patch
Patch4:		%{name}-am15.patch
Patch5:		%{name}-missing_gnomecard_help.patch
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
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
- gnomecal - personal calendar and todo list,
- gnomecard - contact list of friends and business associates.

%description -l es
El administrador de informaciones personales del GNOME consiste de
aplicaciones para hacer su vida muy mas fácil. 
Actualmente estas aplicaciones están presentes:
- gnomecal:  calendario personal,
- gnomecard: lista de contactos.

%description -l pl
Pakiet zawiera aplikacje robi±ce Twoje zapracowane ¿ycie prostrzym.
Aktualnie dwie aplikacje s± obecne:
- gnomecal - prywatny terminarz i lista zadañ
- gnomecard - notatnik z kontaktami przyjació³ oraz partnerów
  biznesowych.

%description -l pt_BR
O gerente de informações pessoais do GNOME consiste de aplicações para
manter sua vida mais fácil. 
Atualmente estes são os aplicativos disponíveis:
- gnomecal : calendário pessoal e lista de coisas a fazer,
- gnomecard: lista de contatos: amigos e parceiros comerciais.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%config %{_sysconfdir}/CORBA/servers/*
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Office/PIMs/*
%{_datadir}/mime-info/gnome-pim.keys
%{_pixmapsdir}/*
