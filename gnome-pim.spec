
%define		snap		20030114

Summary:	GNOME Personal Information Manager
Summary(es):	El administrador de informaciones personales del GNOME
Summary(ja):	The GNOME �Ŀ;�������ޥ͡�����
Summary(pl):	Osobisty terminarz i zarz�dzanie list� zada�
Summary(pt_BR):	O gerenciador de informa��es pessoais do GNOME
Summary(ru):	������������ �������������� �������� (PIM) ��� GNOME
Summary(uk):	������������ �������æ���� �������� (PIM) ��� GNOME
Summary(zh_CN):	GNOME������Ϣ������
Name:		gnome-pim
Version:	1.91.1
Release:	1.%{snap}
Epoch:		1
License:	GPL
Group:		X11/Applications
#Source0:	http://me.in-berlin.de/~jroger/gnome-pim/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{snap}.tar.bz2
Patch0:		%{name}-desktop_location.patch
Patch1:		%{name}-schemas.patch
Icon:		gnome-pim.xpm
URL:		http://www.gnome.org/
BuildRequires:	libmimedir-devel >= 0.2.1-1.20030114
BuildRequires:	libgnomeui-devel >= 2.1.90
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
GNOME �Ŀ;�������ޥ͡�����ˤϡ�˻�������������äȳڤˤ��Ƥ���
�륢�ץꥱ������󤬴ޤޤ�Ƥ��ޤ���
���ߡ��ʲ��Υ��ץꥱ������󤬻Ȥ��ޤ�:
- gnomecal : �ѡ����ʥ�ʥ��������� To Do �ꥹ��
- gnomecard: ͧ�ͤ�ӥ��ͥ��ط��Ԥ�Ϣ����ꥹ��

%description -l pl
Pakiet zawiera aplikacje czyni�ce Twoje zapracowane �ycie prostszym.
Aktualnie zawiera dwie aplikacje:
- gnomecal : prywatny terminarz i lista zada�
- gnomecard: notatnik z kontaktami przyjaci� oraz partner�w w
  interesach.

%description -l pt_BR
O gerente de informa��es pessoais do GNOME consiste de aplica��es para
manter sua vida mais f�cil. Atualmente estes s�o os aplicativos
dispon�veis:
- gnomecal : calend�rio pessoal e lista de coisas a fazer,
- gnomecard: lista de contatos: amigos e parceiros comerciais.

%description -l ru
������������ �������������� �������� ������� �� ����������,
����������� ����� ������� �����. � ��������� ����� ��� ���������
���������:
- gnomecal : ������������ ��������� � ������ ��� (todo)
- gnomecard: ������ ���������

%description -l uk
������������ �������æ���� �������� ����������� � ���������� �������,
�� ���������� ����� �������� �����. ����ڦ �� ������Φ ��������:
- gnomecal : ������������ �������� �� ������ ����� (todo)
- gnomecard: ������ ������Ԧ�

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh
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
%{_datadir}/applications/*
%{_datadir}/idl/*
%{_datadir}/mime-info/gnome-pim.keys
%{_datadir}/gnomecard
%{_datadir}/gnomecal
%{_omf_dest_dir}/*
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/*
