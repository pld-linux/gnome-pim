Summary:	GNOME Personal Information Manager
Summary(es):	El administrador de informaciones personales del GNOME
Summary(ja):	The GNOME 個人情報管理マネージャ
Summary(pl):	Osobisty terminarz i zarz�dzanie list� zada�
Summary(pt_BR):	O gerenciador de informa苺es pessoais do GNOME
Summary(ru):	霤厶藁遡慘拱 瀕届厖礎貧領拱 妖療綴賭 (PIM) 通� GNOME
Summary(uk):	霤厶藁遡慘品 ξ届厖礎κ良� 妖療綴賭 (PIM) 通� GNOME
Summary(zh_CN):	GNOME倖繁佚連砿尖垢醤
Name:		gnome-pim
Version:	1.91.1
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://me.in-berlin.de/%7Ejroger/gnome-pim/%{name}-%{version}.tar.bz2
Icon:		gnome-pim.xpm
URL:		http://www.gnome.org/
BuildRequires:	libmimedir-devel >= 0.2.0
BuildRequires:	libgnomeui-devel >= 2.1.5
Obsoletes:	gnome-pim-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Pakiet zawiera aplikacje czyni�ce Twoje zapracowane �ycie prostszym.
Aktualnie zawiera dwie aplikacje:
- gnomecal : prywatny terminarz i lista zada�
- gnomecard: notatnik z kontaktami przyjaci鶻 oraz partner�w w
  interesach.

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
- gnomecal : 佚厶藁遡慘拱 冒姪猟倉� � 嗤瓶亘 津� (todo)
- gnomecard: 嗤瓶亘 墨淋阻塹�

%description -l uk
霤厶藁遡慘品 ξ届厖礎κ良� 妖療綴賭 嗚盟珍ぴ慯� � 侑彬盟栂蛭 侑惑卅�,
殤 佻姪配媽墮 嵒墺� 攸蔑冱蛭 明津�. 鄙卅擘 壇 料嘖孃陸 侑惑卅揺:
- gnomecal : 佚厶藁遡慘品 冒姪猟倉 堊 嗤瓶亘 嗤卅� (todo)
- gnomecard: 嗤瓶亘 墨淋阻圖�

%prep
%setup  -q

%build
%configure \
	--enable-nls \
	--without-included-gettext \
	--disable-schemas-install
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
%{_datadir}/appslications/*
%{_datadir}/idl/*
%{_datadir}/mime-info/gnome-pim.keys
%{_datadir}/gnomecard
%{_omf_dest_dir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
