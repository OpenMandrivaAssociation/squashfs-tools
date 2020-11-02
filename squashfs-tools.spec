%define oname squashfs
%define _disable_ld_no_undefined 1

Name:		%{oname}-tools
Version:	4.4
Release:	3
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/squashfs/squashfs/squashfs%{version}/%{oname}%{version}.tar.gz
Patch0:	0001-squashfs-tools-fix-build-failure-against-gcc-10.patch
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
%autosetup -n %{oname}%{version} -p1

%build
%setup_compile_flags

cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make_build -j1 ZSTD_SUPPORT=1 XZ_SUPPORT=1 LZO_SUPPORT=1 LZ4_SUPPORT=1 COMP_DEFAULT=zstd EXTRA_CFLAGS="%{optflags}"

%install
install -m755 squashfs-tools/mksquashfs -D %{buildroot}%{_bindir}/mksquashfs
install -m755 squashfs-tools/unsquashfs -D %{buildroot}%{_bindir}/unsquashfs

%files
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
