%define sqname	squashfs
%define sqver	4.2
%define release	8
%define	Summary	Utilities for the creation of compressed squashfs images

Name:		%{sqname}-tools
Version:	%{sqver}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}%{sqver}.tar.gz
Patch0:         buffer-issue.patch
Patch1:         path-issue.patch
BuildRequires:	zlib-devel attr-devel lzma-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{sqname}%{sqver}
%patch0 -p0
%patch1 -p1

%build
cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make XZ_SUPPORT=1 COMP_DEFAULT=xz EXTRA_CFLAGS="%optflags -fuse-ld=bfd"

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
cd squashfs-tools
install -m 755 mksquashfs unsquashfs %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
#%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 4.2-2mdv2011.0
+ Revision: 670011
- mass rebuild

* Thu Mar 03 2011 Thomas Backlund <tmb@mandriva.org> 4.2-1
+ Revision: 641397
- update to 4.2 final

* Fri Feb 04 2011 Thomas Backlund <tmb@mandriva.org> 4.2-0.20101231.1
+ Revision: 635983
- drop S1: lzma465 sdk
- update to cvs 20101231 to get xz support
- build and use xz support by default

* Wed Oct 20 2010 Thomas Backlund <tmb@mandriva.org> 4.1-1mdv2011.0
+ Revision: 586918
- update to 4.1

* Tue Dec 29 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.0-3.20091221.1mdv2010.1
+ Revision: 483266
- add lzma support to mksquashfs/unsquashfs

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.0-2mdv2010.0
+ Revision: 427213
- rebuild

* Mon Apr 06 2009 Pascal Terjan <pterjan@mandriva.org> 4.0-1mdv2009.1
+ Revision: 364374
- Update to 4.0 final

* Wed Feb 18 2009 Pascal Terjan <pterjan@mandriva.org> 4.0-0.20090125.1mdv2009.1
+ Revision: 342394
- Update to a cvs snapshot able to create v4 fs so that we can mount them
  (we lose unsquashfs for now)

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 3.3-4mdv2009.0
+ Revision: 140851
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Olivier Blin <oblin@mandriva.com> 3.3-4mdv2008.1
+ Revision: 119554
- fix hang when dealing with sparse files (patch from CVS)

  + Thierry Vignaud <tv@mandriva.org>
    - fix description

* Thu Dec 13 2007 Olivier Blin <oblin@mandriva.com> 3.3-3mdv2008.1
+ Revision: 119429
- package unsquashfs

* Wed Dec 12 2007 Olivier Blin <oblin@mandriva.com> 3.3-2mdv2008.1
+ Revision: 119020
- rebuild with latest lzma static library to fix zlib support
- update sqlzma2u-3.3.patch from sqlzma3.3-fixed.tar.bz2

* Wed Nov 14 2007 Olivier Blin <oblin@mandriva.com> 3.3-1mdv2008.1
+ Revision: 108685
- 3.3
- update lzma patch and headers
- rediff nolzma patch


* Wed Mar 07 2007 Olivier Blin <oblin@mandriva.com> 3.2-1.r2.2mdv2007.0
+ Revision: 134240
- do not use lzma by default and document a new -lzma option
- add lzma support (from squashfs-lzma.org)

* Tue Feb 13 2007 Olivier Blin <oblin@mandriva.com> 3.2-1.r2.1mdv2007.1
+ Revision: 120480
- 3.2-r2
- Import squashfs-tools

* Sat Sep 02 2006 Arnaud Patard <apatard@mandriva.com> 3.1.1.r2.1mdv2007.0
- 3.1-r2

* Thu Aug 31 2006 Arnaud Patard <apatard@mandriva.com> 3.1-1mdv2007.0
- 3.1

* Mon Jan 23 2006 Arnaud Patard <apatard@mandriva.com> 2.2-1.r2.1mdk
- 2.2-r2

* Tue Mar 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.1-1.r2.1mdk
- 2.1-r2
- cosmetics

* Thu Jul 15 2004 Jaco Greeff <jaco@mandrake.org> 2.0-1mdk
- Version 2.0

