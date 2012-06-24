Summary:	GNOME Personal Information Manager
Summary(es):	El administrador de informaciones personales del GNOME
Summary(ja):	The GNOME �Ŀ;�������ޥ͡�����
Summary(pl):	Osobisty terminarz i zarz�dzanie list� zada�
Summary(pt_BR):	O gerenciador de informa��es pessoais do GNOME
Summary(ru):	������������ �������������� �������� (PIM) ��� GNOME
Summary(uk):	������������ �������æ���� �������� (PIM) ��� GNOME
Summary(zh_CN):	GNOME������Ϣ������
Name:		gnome-pim
Version:	1.4.6
Release:	0.3
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-pim/%{name}-%{version}.tar.gz
# Patch0:	%{name}-fontset.patch
Patch1:		%{name}-gettext.patch
Patch2:		%{name}-macros.patch
Patch4:		%{name}-am15.patch
Patch5:		%{name}-missing_dirs.patch
Patch6:		%{name}-1.4.6-pl.patch
Patch7:		%{name}-shortcut.diff
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
# %patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I macros
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
%{_datadir}/idl/*
%{_pixmapsdir}/*
