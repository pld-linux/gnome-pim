Summary:	GNOME Personal Information Manager
Summary(es):	El administrador de informaciones personales del GNOME
Summary(ja):	The GNOME ╦д©м╬ПйС╢имЩ╔ч╔м║╪╔╦╔Ц
Summary(pl):	Osobisty terminarz i mened©er harmonogramСw
Summary(pt_BR):	O gerenciador de informaГУes pessoais do GNOME
Summary(ru):	Персональный информационный менеджер (PIM) для GNOME
Summary(uk):	Персональний ╕нформац╕йний менеджер (PIM) для GNOME
Summary(zh_CN):	GNOME╦Жхкпео╒╧эюМ╧╓╬ъ
Name:		gnome-pim
Version:	1.4.6
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-pim/1.4/%{name}-%{version}.tar.gz
# Source0-md5:	a694c66ab5431c8bee36323758beb3c0
Patch0:		%{name}-fontset.patch
Patch1:		%{name}-gettext.patch
Patch2:		%{name}-macros.patch
Patch3:		%{name}-gnomecal.patch
Patch4:		%{name}-am15.patch
Patch5:		%{name}-missing_gnomecard_help.patch
Patch6:		%{name}-pl.patch
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
- gnomecal : personal calendar and todo list,
- gnomecard: contact list of friends and business associates.

%description -l es
El administrador de informaciones personales del GNOME consiste de
aplicaciones para hacer su vida muy mas fАcil. Actualmente estas
aplicaciones estАn presentes:
- gnomecal : calendario personal,
- gnomecard: lista de contactos.

%description -l ja
GNOME ╦д©м╬ПйС╢имЩ╔ч╔м║╪╔╦╔Ц╓к╓о║╒к╩╓╥╓╓кХфЭ╓Р╓а╓Г╓ц╓хЁз╓к╓╥╓ф╓╞╓Л
╓К╔╒╔в╔Й╔╠║╪╔╥╔Г╔С╓╛╢ч╓ч╓Л╓ф╓╓╓ч╓╧║ё
╦╫╨ъ║╒╟й╡╪╓н╔╒╔в╔Й╔╠║╪╔╥╔Г╔С╓╛╩х╓╗╓ч╓╧:

 - gnomecal : ╔я║╪╔╫╔й╔К╓й╔╚╔Л╔С╔ю║╪╓х To Do ╔Й╔╧╔х
 - gnomecard: м╖©м╓Д╔с╔╦╔м╔╧╢ь╥╦╪т╓но╒мМюХ╔Й╔╧╔х

%description -l pl
Pakiet zawiera aplikacje robi╠ce Twoje zapracowane ©ycie prostrzym.
Aktualnie dwie aplikacje s╠ obecne:
- gnomecal : prywatny terminarz i lista zadaЯ
- gnomecard: notatnik z kontaktami przyjaciСЁ oraz partnerСw
  biznesowych.

%description -l pt_BR
O gerente de informaГУes pessoais do GNOME consiste de aplicaГУes para
manter sua vida mais fАcil. Atualmente estes sЦo os aplicativos
disponМveis:
- gnomecal : calendАrio pessoal e lista de coisas a fazer,
- gnomecard: lista de contatos: amigos e parceiros comerciais.

%description -l ru
Персональный информационный менеджер состоит из приложений,
облегчающих жизнь занятых людей. В настоящее время это следующие
программы:

 - gnomecal : персональный календарь и список дел (todo)
 - gnomecard: список контактов

%description -l uk
Персональний ╕нформац╕йний менеджер склада╓ться з прикладних програм,
що полегшують життя зайнятих людей. Нараз╕ це наступн╕ програми:

 - gnomecal : персональний календар та список справ (todo)
 - gnomecard: список контакт╕в

%prep
%setup  -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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
	Productivitydir=%{_applnkdir}/Office/PIMs

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
%{_pixmapsdir}/*
