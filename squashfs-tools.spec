%define oname squashfs

Summary:	Utilities for the creation of compressed squashfs images
Name:		%{oname}-tools
Version:	4.2
Release:	9
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/squashfs/squashfs/squashfs%{version}/%{oname}%{version).tar.gz
Patch0:		buffer-issue.patch
Patch1:		path-issue.patch
BuildRequires:	zlib-devel
BuildRequires:	attr-devel
BuildRequires:	lzma-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{oname}%{version}
%patch0 -p0
%patch1 -p1

%build
%setup_compile_flags
cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make XZ_SUPPORT=1 COMP_DEFAULT=xz EXTRA_CFLAGS="%optflags -fuse-ld=bfd"

%install
install -d %{buildroot}%{_bindir}
cd squashfs-tools
install -m 755 mksquashfs unsquashfs %{buildroot}%{_bindir}

%files
#%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs

