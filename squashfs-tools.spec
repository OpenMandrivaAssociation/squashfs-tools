%define oname squashfs
%define _disable_ld_no_undefined 1

Name:		%{oname}-tools
Version:	4.7.4
Release:	1
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		https://github.com/plougher/squashfs-tools
Source0:	https://github.com/plougher/squashfs-tools/archive/refs/tags/%{version}.tar.gz
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libattr)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(lzo2)
BuildRequires:	pkgconfig(libzstd)

%description
squashfs-tools are utilities for the creation
of compressed squashfs images.

%prep
%autosetup -p1

%build
%set_build_flags

cd squashfs-tools
%make_build -j1 ZSTD_SUPPORT=1 XZ_SUPPORT=1 LZMA_XZ_SUPPORT=1 LZO_SUPPORT=1 LZ4_SUPPORT=1 COMP_DEFAULT=zstd EXTRA_CFLAGS="%{optflags}"

%install
install -m755 squashfs-tools/mksquashfs -D %{buildroot}%{_bindir}/mksquashfs
install -m755 squashfs-tools/unsquashfs -D %{buildroot}%{_bindir}/unsquashfs

%files
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
