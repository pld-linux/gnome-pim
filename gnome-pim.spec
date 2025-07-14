
%define		snap		20030114

Summary:	GNOME Personal Information Manager
Summary(es.UTF-8):	El administrador de informaciones personales del GNOME
Summary(ja.UTF-8):	The GNOME 個人情報管理マネージャ
Summary(pl.UTF-8):	Osobisty terminarz i zarządzanie listą zadań
Summary(pt_BR.UTF-8):	O gerenciador de informações pessoais do GNOME
Summary(ru.UTF-8):	Персональный информационный менеджер (PIM) для GNOME
Summary(uk.UTF-8):	Персональний інформаційний менеджер (PIM) для GNOME
Summary(zh_CN.UTF-8):	GNOME个人信息管理工具
Name:		gnome-pim
Version:	1.91.1
Release:	1.%{snap}
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://me.in-berlin.de/~jroger/gnome-pim/%{name}-%{version}.tar.gz
# Source0-md5:	3aee416596b6b5a5f3f564700c73f562
Patch0:		%{name}-desktop_location.patch
Patch1:		%{name}-schemas.patch
URL:		http://www.gnome.org/
BuildRequires:	libgnomeui-devel >= 2.1.90
BuildRequires:	libmimedir-devel >= 0.2.1-1.20030114
Obsoletes:	gnome-pim-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNOME Personal Information Manager consists of applications to
make keeping up with your busy life easier. Currently these apps are
present:
- gnomecal : personal calendar and todo list,
- gnomecard: contact list of friends and business associates.

%description -l es.UTF-8
El administrador de informaciones personales del GNOME consiste de
aplicaciones para hacer su vida muy mas fácil. Actualmente estas
aplicaciones están presentes:
- gnomecal : calendario personal,
- gnomecard: lista de contactos.

%description -l ja.UTF-8
GNOME 個人情報管理マネージャには、忙しい毎日をちょっと楽にしてくれ
るアプリケーションが含まれています。
現在、以下のアプリケーションが使えます:
- gnomecal : パーソナルなカレンダーと To Do リスト
- gnomecard: 友人やビジネス関係者の連絡先リスト

%description -l pl.UTF-8
Pakiet zawiera aplikacje czyniące Twoje zapracowane życie prostszym.
Aktualnie zawiera dwie aplikacje:
- gnomecal : prywatny terminarz i lista zadań
- gnomecard: notatnik z kontaktami przyjaciół oraz partnerów w
  interesach.

%description -l pt_BR.UTF-8
O gerente de informações pessoais do GNOME consiste de aplicações para
manter sua vida mais fácil. Atualmente estes são os aplicativos
disponíveis:
- gnomecal : calendário pessoal e lista de coisas a fazer,
- gnomecard: lista de contatos: amigos e parceiros comerciais.

%description -l ru.UTF-8
Персональный информационный менеджер состоит из приложений,
облегчающих жизнь занятых людей. В настоящее время это следующие
программы:
- gnomecal : персональный календарь и список дел (todo)
- gnomecard: список контактов

%description -l uk.UTF-8
Персональний інформаційний менеджер складається з прикладних програм,
що полегшують життя зайнятих людей. Наразі це наступні програми:
- gnomecal : персональний календар та список справ (todo)
- gnomecard: список контактів

%prep
%setup  -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure \
	--enable-nls \
	--without-included-gettext \
	--disable-install-schemas
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/idl/*
%{_datadir}/mime-info/gnome-pim.keys
%{_datadir}/gnomecard
%{_datadir}/gnomecal
%{_omf_dest_dir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
