Summary:	CLIPS - a productive development and delivery expert system tool
Summary(pl):	CLIPS - narzêdzie do tworzenia i wdra¿ania systemów eksperckich
Name:		clips
Version:	6.2
Release:	1
License:	Public Domain
Group:		Development/Languages
Source0:	http://www.ghg.net/clips/download/source/clipssrc.tar.Z
Source1:	http://www.ghg.net/clips/download/documentation/3CCP.pdf
Source2:	http://www.ghg.net/clips/download/documentation/abstract.pdf
Source3:	http://www.ghg.net/clips/download/documentation/apg.pdf
Source4:	http://www.ghg.net/clips/download/documentation/arch5-1.pdf
Source5:	http://www.ghg.net/clips/download/documentation/bpg.pdf
Source6:	http://www.ghg.net/clips/download/documentation/ig.pdf
Source7:	http://www.ghg.net/clips/download/documentation/usrguide.pdf
Source8:	http://www.ghg.net/clips/download/source/%{name}.hlp
# from http://www.ghg.net/clips/download/executables/examples/
Source9:	%{name}-examples-%{version}.tar.gz
Patch0:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
URL:		http://www.ghg.net/clips/CLIPS.html
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
libtoolize --copy --force
aclocal
autoheader
autoconf
automake -a -c

echo '#undef HELP_DEFAULT' > usrsetup.h
echo '#define HELP_DEFAULT "%{_datadir}/misc/%{name}.hlp"' >> usrsetup.h

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C clipssrc DESTDIR=$RPM_BUILD_ROOT install

install %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} \
	%{SOURCE6} %{SOURCE7} .

install -d $RPM_BUILD_ROOT%{_datadir}/misc/
install %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/misc/%{name}.hlp

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
gzip -9nf < readme.txt > COPYING.gz

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
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
