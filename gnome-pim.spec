# TODO:
#  - fix gnomecal conduit - libcalendar_conduit (linking problem ?)
#  - fix conduits i18n (proper gettext domain binding)
#
%bcond_without	pilot_support

Summary:	GNOME Personal Information Manager
Summary(es):	El administrador de informaciones personales del GNOME
Summary(ja):	The GNOME 個人情報管理マネージャ
Summary(pl):	Osobisty terminarz i mened�er harmonogram�w
Summary(pt_BR):	O gerenciador de informa苺es pessoais do GNOME
Summary(ru):	霤厶藁遡慘拱 瀕届厖礎貧領拱 妖療綴賭 (PIM) 通� GNOME
Summary(uk):	霤厶藁遡慘品 ξ届厖礎κ良� 妖療綴賭 (PIM) 通� GNOME
Summary(zh_CN):	GNOME倖繁佚連砿尖垢醤
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
aplicaciones para hacer su vida muy mas f�cil. Actualmente estas
aplicaciones est�n presentes:
- gnomecal : calendario personal,
- gnomecard: lista de contactos.

%description -l ja
GNOME 個人情報管理マネージャには、忙しい毎日をちょっと楽にしてくれ
るアプリケーションが含まれています。
現在、以下のアプリケーションが使えます:
- gnomecal : パーソナルなカレンダーと To Do リスト
- gnomecard: 友人やビジネス関係者の連絡先リスト

%description -l pl
Pakiet zawiera aplikacje robi�ce Twoje zapracowane �ycie prostrzym.
Aktualnie dwie aplikacje s� obecne:
- gnomecal : prywatny terminarz i lista zada�,
- gnomecard: notatnik z kontaktami przyjaci鶻 oraz partner�w
  biznesowych.

%description -l pt_BR
O gerente de informa苺es pessoais do GNOME consiste de aplica苺es para
manter sua vida mais f�cil. Atualmente estes s�o os aplicativos
dispon�veis:
- gnomecal : calend�rio pessoal e lista de coisas a fazer,
- gnomecard: lista de contatos: amigos e parceiros comerciais.

%description -l ru
霤厶藁遡慘拱 瀕届厖礎貧領拱 妖療綴賭 嗜嘖鷲� 冨 侑斌�崚良�,
和姪媒狙殄� 嵒變� 攸倫壅� 明津�. � 料嘖湾歸� 徠斗� 榑� 嗅田媽殄�
侑惑卅様�:
- gnomecal : 佚厶藁遡慘拱 冒姪猟倉� � 嗤瓶亘 津� (todo),
- gnomecard: 嗤瓶亘 墨淋阻塹�.

%description -l uk
霤厶藁遡慘品 ξ届厖礎κ良� 妖療綴賭 嗚盟珍ぴ慯� � 侑彬盟栂蛭 侑惑卅�,
殤 佻姪配媽墮 嵒墺� 攸蔑冱蛭 明津�. 鄙卅擘 壇 料嘖孃陸 侑惑卅揺:
- gnomecal : 佚厶藁遡慘品 冒姪猟倉 堊 嗤瓶亘 嗤卅� (todo),
- gnomecard: 嗤瓶亘 墨淋阻圖�.

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
Pakiet gnome-pim-conduits zawiera 咳cza niezb�dne do komunikacji
PalmPilota z aplikacjami gnome-pim. Aktualnie dwa 咳cza s� obecne:
- gnomecal : do synchronizacji prywatny terminarz GnomeCala z
             kalendarzem Palm-Pilota,
- gnomecard: do synchronizacji listy kontakt�w.

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
#%{_datadir}/gnome-pilot/conduits/gnomecal*
%{_datadir}/gnome-pilot/conduits/gnomecar*
%endif
