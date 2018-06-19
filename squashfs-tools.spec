%define	oname squashfs
%define _disable_ld_no_undefined 1

Name:		%{oname}-tools
Version:	4.3
Release:	12
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/squashfs/squashfs/squashfs%{version}/%{oname}%{version}.tar.gz
# From master branch (55f7ba830d40d438f0b0663a505e0c227fc68b6b).
# 32 bit process can use too much memory when using PAE or 64 bit kernels
Patch0:		PAE.patch
# From master branch (604b607d8ac91eb8afc0b6e3d917d5c073096103).
# Prevent overflows when using the -mem option.
Patch1:		mem-overflow.patch
# From squashfs-devel@lists.sourceforge.net by Guan Xin <guanx.bac@gmail.com>
# For https://bugzilla.redhat.com/show_bug.cgi?id=1141206
Patch2:		2gb.patch
# (tpg) add zstd support
# https://github.com/iburinoc/squashfs-tools/tree/zstd
#Patch3:		0000-Add-Zstandard-support.patch
#Patch4:		0001-Add-patch-for-GENERIC-instead-of-dstSize_tooSmall-bu.patch
# (tpg) patch taken from https://github.com/facebook/zstd/tree/dev/contrib/linux-kernel
Patch5:   0006-squashfs-tools-Add-zstd-support.patch

BuildRequires:	pkgconfig(zlib)
BuildRequires:	attr-devel
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	lzo-devel
BuildRequires:	pkgconfig(libzstd)

%description
squashfs-tools are utilities for the creation
of compressed squashfs images.

%prep
%setup -q -n %{oname}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p0
%patch5 -p1

%build
%setup_compile_flags

cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make -j1 ZSTD_SUPPORT=1 XZ_SUPPORT=1 LZO_SUPPORT=1 LZ4_SUPPORT=1 COMP_DEFAULT=zstd EXTRA_CFLAGS="%{optflags}"

%install
install -m755 squashfs-tools/mksquashfs -D %{buildroot}%{_bindir}/mksquashfs
install -m755 squashfs-tools/unsquashfs -D %{buildroot}%{_bindir}/unsquashfs

%files
%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
