# $Id$
# Authority: matthias

Summary: Utility to copy DVD .vob files to disk
Name: vobcopy
Version: 0.5.16
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://vobcopy.org/projects/c/c.shtml
Source: http://vobcopy.org/download/vobcopy-%{version}.tar.bz2
Patch0: vobcopy-0.5.16-Makefile.patch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libdvdread
BuildRequires: libdvdread-devel

%description
Vobcopy copies DVD .vob files to disk, decrypting them on the way (thanks to
libdvdread and libdvdcss) and merges them into file(s) with the name extracted
from the DVD. There is one drawback though: at the moment vobcopy doesn't deal
with multi-angle-dvd's. But since these are rather sparse this shouldn't
matter much.


%prep 
%setup -q
%patch0 -p1 -b .Makefile


%build 
%{__make} \
    CFLAGS="%{optflags}" \
    BINDIR="%{_bindir}" \
    MANDIR="%{_mandir}"


%install 
%{__rm} -rf %{buildroot}
%{__make} install \
    BINDIR="%{buildroot}%{_bindir}" \
    MANDIR="%{buildroot}%{_mandir}"


%clean 
%{__rm} -rf %{buildroot}


%files 
%defattr(-, root, root, 0755) 
%doc Changelog COPYING README Release-Notes TODO
%doc alternative_programs.txt
%{_bindir}/vobcopy
%{_mandir}/man1/vobcopy.1*
%lang(de) %{_mandir}/de/man1/vobcopy.1*


%changelog
* Mon Mar 27 2006 Matthias Saou <http://freshrpms.net/> 0.5.16-1
- Major spec file cleanup.

* Fri Jan 6 2006 Robos  <robos@muon.de>
- 0.5.16: -see changelog

* Fri Jul 29 2005 Robos  <robos@muon.de>
- 0.5.15: -option to skip already present files with -m. 
  	  copying of dvd's with files ending in ";?" should work now.

* Sun Oct 24 2004 Robos  <robos@muon.de>
- 0.5.14-rc1: - misc *bsd fixes and first straight OSX support

* Mon Mar 7 2004 Robos  <robos@muon.de>
- 0.5.12-1: -m off-by-one error fixed

* Mon Jan 19 2004 Robos <robos@muon.de>
- 0.5.10-1: -O now works 
  	    cleanup



* Wed Nov 13 2003 Robos <robos@muon.de>
- 0.5.9-1: -F now accepts factor number
  	   cleanups and small bugfix
  	   new vobcopy.spec

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- 0.5.8-2: libdvdread is now a pre-requisite

* Sun Nov 09 2003 Florin Andrei <florin@andrei.myip.org>
- first package, 0.5.8-1
