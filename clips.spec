Summary:	CLIPS - a productive development and delivery expert system tool
Summary(pl):	CLIPS - narz�dzie do tworzenia i wdra�ania system�w eksperckich
Name:		clips
Version:	6.1
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	http://www.ghgcorp.com/clips/download/other/%{name}6.tgz
Source1:	3CCP.pdf
Source2:	abstract.pdf
Source3:	apg.pdf
Source4:	arch5-1.pdf
Source5:	bpg.pdf
Source6:	ig.pdf
Source7:	usrguide.pdf
URL:		http://www.ghgcorp.com/clips/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLIPS is a productive development and delivery expert system tool
which provides a complete environment for the construction of rule
and/or object based expert systems. CLIPS is being used by numerous
users throughout the public and private community including: all NASA
sites and branches of the military, numerous federal bureaus,
government contractors, universities, and many companies.

%description -l pl
CLIPS jest narz�dziem do tworzenia i wdra�ania system�w eksperckich
zapewniaj�cym kompletne �rodowisko do tworzenia system�w eksperckich
opartych na regu�ach lub obiektach. CLIPS jest u�ywany przez wielu
u�ytkownik�w prywatnych i publicznych, tym: NASA i r�ne ga��zie
wojska, biura federalne, kontrahent�w rz�dowych, uniwersytety i wiele
firm.

%package doc
Summary:	CLIPS documentation
Summary(pl):	Dokumentacja do CLIPS
Group:		Development/Languages

%description doc
CLIPS documentation.

%description doc -l pl
Dokumentacja do CLIPS.

%prep
%setup -q -n %{name}%{version}

%build
%configure2_13
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	%{SOURCE6} %{SOURCE7} .

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/clips
%attr(755,root,root) %{_libdir}/libClips*

%files doc
%defattr(644,root,root,755)
%doc 3CCP.pdf abstract.pdf apg.pdf arch5-1.pdf bpg.pdf
%doc ig.pdf usrguide.pdf
