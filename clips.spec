Summary:	CLIPS - a productive development and delivery expert system tool
Summary(pl):	CLIPS - narzêdzie do tworzenia i wdra¿ania systemów eksperckich
Name:		clips
Version:	6.2
Release:	1
License:	Public Domain
Group:		Development/Languages
Source0:	http://www.ghg.net/clips/download/source/clipssrc.tar.Z
# Source0-md5:	de2bddd67d3f82f23fb6c1bef051b544
Source1:	http://www.ghg.net/clips/download/documentation/3CCP.pdf
# Source1-md5:	a6a60733af08f9e9e6d0928272ad4dd9
Source2:	http://www.ghg.net/clips/download/documentation/abstract.pdf
# Source2-md5:	cd3ecddc4e538b8af0e5cf08ab7fd89c
Source3:	http://www.ghg.net/clips/download/documentation/apg.pdf
# Source3-md5:	77a051086c3be543f507e8b1f77f7077
Source4:	http://www.ghg.net/clips/download/documentation/arch5-1.pdf
# Source4-md5:	9a13d2ed18fe6ab67902d5bce29957cb
Source5:	http://www.ghg.net/clips/download/documentation/bpg.pdf
# Source5-md5:	15190fdc0895356ab347e1dd41bb6aa7
Source6:	http://www.ghg.net/clips/download/documentation/ig.pdf
# Source6-md5:	ab5d7fb340c3be4dc533831dc7d8f1b5
Source7:	http://www.ghg.net/clips/download/documentation/usrguide.pdf
# Source7-md5:	f2da81e30713f24d8b94c2822fc7704a
Source8:	http://www.ghg.net/clips/download/source/%{name}.hlp
# Source8-md5:	e6429bcd668b085038179cf54764436a
# from http://www.ghg.net/clips/download/executables/examples/
Source9:	%{name}-examples-%{version}.tar.gz
# Source9-md5:	83dfad948a07267487661973435d72e9
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

%description -l pl
CLIPS jest narzêdziem do tworzenia i wdra¿ania systemów eksperckich
zapewniaj±cym kompletne ¶rodowisko do tworzenia systemów eksperckich
opartych na regu³ach lub obiektach. CLIPS jest u¿ywany przez wielu
u¿ytkowników prywatnych i publicznych, tym: NASA i ró¿ne ga³êzie
wojska, biura federalne, kontrahentów rz±dowych, uniwersytety i wiele
firm.

%package doc
Summary:	CLIPS documentation
Summary(pl):	Dokumentacja do CLIPS
Group:		Development/Languages

%description doc
CLIPS documentation and examples.

%description doc -l pl
Dokumentacja i przyk³ady do CLIPSa.

%package devel
Summary:	CLIPS development files
Summary(pl):	Nag³ówki do CLIPSa
Group:		Development/Languages

%description devel
Includes for programs using embadded CLIPS enviroment.

%description devel -l pl
Pliki nag³ówkowe dla programów u¿ywaj±cych wbudowanego ¶rodowiska CLIPSa.

%package static
Summary:	CLIPS static libraries
Summary(pl):	Statyczne biblioteki do CLIPSa
Group:		Development/Languages

%description static
Static libraries for programs using embadded CLIPS enviroment.

%description devel -l pl
Statyczne biblioteki dla programów u¿ywaj±cych wbudowanego ¶rodowiska 
CLIPSa.

%prep
%setup -q -T -c
tar zxf %{SOURCE0}
%patch0 -p0
tar zxf %{SOURCE9}

%build
cd clipssrc
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

%{__make} -C clipssrc install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	%{SOURCE6} %{SOURCE7} .

install %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/misc/%{name}.hlp

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

mv readme.txt COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
