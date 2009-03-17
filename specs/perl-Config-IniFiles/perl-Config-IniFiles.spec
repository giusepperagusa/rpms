# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-IniFiles

Summary: Module for reading .ini-style configuration files
Name: perl-Config-IniFiles
Version: 2.47
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-IniFiles/

Source: http://www.cpan.org/modules/by-module/Config/Config-IniFiles-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker) >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Module for reading .ini-style configuration files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/IniFiles.pm

%changelog
* Tue Mar 17 2009 Dries Verachtert <dries@ulyssis.org> - 2.47-1
- Updated to release 2.47.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.39-1
- Updated to release 2.39.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 2.38-2
- Cosmetic changes.

* Sun Mar 07 2004 Dag Wieers <dag@wieers.com> - 2.38-1
- Initial package. (using DAR)
