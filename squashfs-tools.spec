%bcond_without	uclibc

%define	oname	squashfs
Name:		%{oname}-tools
Version:	4.2
Release:	12
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/squashfs/squashfs/squashfs%{version}/%{oname}%{version}.tar.gz
Patch0:		buffer-issue.patch
Patch1:		path-issue.patch
BuildRequires:	pkgconfig(zlib) attr-devel pkgconfig(liblzma)
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
squashfs-tools are utilities for the creation
of compressed squashfs images.

%package -n	uclibc-%{name}
Summary:	Utilities for the creation of compressed squashfs images (uClibc build)
Group:		Networking/File transfer

%description -n	uclibc-%{name}
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{oname}%{version}
%patch0 -p0
%patch1 -p1

%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%if %{with uclibc}
pushd .uclibc/squashfs-tools
%make CC=%{uclibc_cc} XZ_SUPPORT=1 COMP_DEFAULT=xz EXTRA_CFLAGS="%{uclibc_cflags} -fuse-ld=bfd"
popd
%endif

%setup_compile_flags
cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make XZ_SUPPORT=1 COMP_DEFAULT=xz EXTRA_CFLAGS="%{optflags} -fuse-ld=bfd"

%install
%if %{with uclibc}
install -m755 .uclibc/squashfs-tools/mksquashfs -D %{buildroot}%{uclibc_root}%{_bindir}/mksquashfs
install -m755 .uclibc/squashfs-tools/unsquashfs -D %{buildroot}%{uclibc_root}%{_bindir}/unsquashfs
%endif

install -m755 squashfs-tools/mksquashfs -D %{buildroot}%{_bindir}/mksquashfs
install -m755 squashfs-tools/unsquashfs -D %{buildroot}%{_bindir}/unsquashfs

%files
%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs

%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/mksquashfs
%{uclibc_root}%{_bindir}/unsquashfs
