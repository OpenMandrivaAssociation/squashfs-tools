%define	sqname	squashfs
Name:		%{sqname}-tools
Version:	4.2
Release:	6
Summary:	Utilities for the creation of compressed squashfs images
License:	GPLv2+
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}%{version}.tar.gz
Patch0:		buffer-issue.patch
Patch1:		path-issue.patch
BuildRequires:	pkgconfig(zlib) attr-devel pkgconfig(liblzma)

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{sqname}%{version}
%patch0 -p0
%patch1 -p1

%build
cd squashfs-tools
# Using BFD ld is a workaround for mksquashfs and unsquashfs getting the
# same build ID with gold
%make XZ_SUPPORT=1 COMP_DEFAULT=xz EXTRA_CFLAGS="%{optflags} -fuse-ld=bfd"

%install
install -d %{buildroot}%{_bindir}
cd squashfs-tools
install -m 755 mksquashfs unsquashfs %{buildroot}%{_bindir}

%files
%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
