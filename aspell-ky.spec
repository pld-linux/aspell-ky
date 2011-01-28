Summary:	Kirghiz dictionary for aspell
Summary(pl.UTF-8):	Słownik kirgiski dla aspella
Name:		aspell-ky
Version:	0.01
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ky/aspell6-ky-%{version}-%{subv}.tar.bz2
# Source0-md5:	83ed490464521361867546f9ad4cbaf2
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60.0
BuildRequires:	which
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kirghiz dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik kirgiski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-ky-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/kirghiz.alias
%{_libdir}/aspell/ky.*
%{_datadir}/aspell/ky.dat
%{_datadir}/aspell/ky_affix.dat
%{_datadir}/aspell/l-ky.*
