Summary:	CLIPS - a productive development and delivery expert system tool
Summary(pl.UTF-8):	CLIPS - narzędzie do tworzenia i wdrażania systemów eksperckich
Name:		clips
Version:	6.26
Release:	3
License:	Public Domain
Group:		Development/Languages
Source0:	http://www.ghg.net/clips/download/source/clipssrc.tar.Z
# Source0-md5:	ccba9d912375e57a1b7d9eba12da4198
Source1:	http://www.ghg.net/clips/download/documentation/3CCP.pdf
# Source1-md5:	a6a60733af08f9e9e6d0928272ad4dd9
Source2:	http://www.ghg.net/clips/download/documentation/abstract.pdf
# Source2-md5:	cd3ecddc4e538b8af0e5cf08ab7fd89c
Source3:	http://www.ghg.net/clips/download/documentation/apg.pdf
# Source3-md5:	fae2267d96fb95603345e91c9990caaa
Source4:	http://www.ghg.net/clips/download/documentation/arch5-1.pdf
# Source4-md5:	9a13d2ed18fe6ab67902d5bce29957cb
Source5:	http://www.ghg.net/clips/download/documentation/bpg.pdf
# Source5-md5:	63891971aa782dc67c2de0579647247e
Source6:	http://www.ghg.net/clips/download/documentation/ig.pdf
# Source6-md5:	89beca5caa08b30d8285cca7f1df1d26
Source7:	http://www.ghg.net/clips/download/documentation/usrguide.pdf
# Source7-md5:	44e54697a8acf3509bc4ca51d88b65bd
Source8:	http://www.ghg.net/clips/download/source/%{name}.hlp
# Source8-md5:	55f662f8aa8400aff8bf5a5cb882f708
Source9:	http://www.ghg.net/clips/download/executables/examples/AllExamples.tar.Z
# Source9-md5:	f5c02b997199f3ede779b8502af2ba09
Patch0:		%{name}-automake.patch
URL:		http://www.ghg.net/clips/CLIPS.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CLIPS is a productive development and delivery expert system tool
which provides a complete environment for the construction of rule
and/or object based expert systems. CLIPS is being used by numerous
users throughout the public and private community including: all NASA
sites and branches of the military, numerous federal bureaus,
government contractors, universities, and many companies.

%description -l pl.UTF-8
CLIPS jest narzędziem do tworzenia i wdrażania systemów eksperckich
zapewniającym kompletne środowisko do tworzenia systemów eksperckich
opartych na regułach lub obiektach. CLIPS jest używany przez wielu
użytkowników prywatnych i publicznych, tym: NASA i różne gałęzie
wojska, biura federalne, kontrahentów rządowych, uniwersytety i wiele
firm.

%package doc
Summary:	CLIPS documentation
Summary(pl.UTF-8):	Dokumentacja do CLIPS
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description doc
CLIPS documentation and examples.

%description doc -l pl.UTF-8
Dokumentacja i przykłady do CLIPSa.

%package devel
Summary:	CLIPS development files
Summary(pl.UTF-8):	Nagłówki do CLIPSa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description devel
Includes for programs using embadded CLIPS enviroment.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programów używających wbudowanego środowiska CLIPSa.

%package static
Summary:	CLIPS static libraries
Summary(pl.UTF-8):	Statyczne biblioteki do CLIPSa
Group:		Development/Languages
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries for programs using embadded CLIPS enviroment.

%description static -l pl.UTF-8
Statyczne biblioteki dla programów używających wbudowanego środowiska
CLIPSa.

%prep
%setup -q -T -c -a0 -a9
%patch0 -p0

%build
cd clipssrc/clipssrc/
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}

echo '#undef HELP_DEFAULT' > usrsetup.h
echo '#define HELP_DEFAULT "%{_datadir}/misc/%{name}.hlp"' >> usrsetup.h

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/misc,%{_examplesdir}/%{name}-%{version}}

%{__make} -C clipssrc/clipssrc install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	%{SOURCE6} %{SOURCE7} .

install %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/misc/%{name}.hlp

cp -r Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -f clipssrc/readme.txt COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/clips
%attr(755,root,root) %{_libdir}/libclips.so.*.*.*
%{_datadir}/misc/%{name}.hlp

%files devel
%defattr(644,root,root,755)
%{_libdir}/libclips.so
%{_libdir}/libclips.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libclips.a

%files doc
%defattr(644,root,root,755)
%doc *.pdf
%{_examplesdir}/%{name}-%{version}
