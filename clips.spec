Summary:	Clips
Name:		clips
Version:	6.1
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	http://www.ghgcorp.com/clips/download/other/clips6.tgz
Source1:	3CCP.pdf
Source2:	abstract.pdf
Source3:	apg.pdf
Source4:	arch5-1.pdf
Source5:	bpg.pdf
Source6:	ig.pdf
Source7:	usrguide.pdf
URL:		http://www.ghgcorp.com/clips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clips

%package doc
Summary:	Clips documentation
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki

%description doc
Clips documentation

%prep
%setup -q -n %{name}%{version}

%build
%configure 
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
