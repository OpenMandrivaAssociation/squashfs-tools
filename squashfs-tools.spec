%define sqname	squashfs
%define sqver	4.1
%define release	%mkrel 1
%define	Summary	Utilities for the creation of compressed squashfs images

Name:		%{sqname}-tools
Version:	%{sqver}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}%{sqver}.tar.gz
Source1:	lzma465.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel attr-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -T -c -b1 -n lzma
%setup -q -n %{sqname}%{sqver}

%build
cd squashfs-tools
%make LZMA_SUPPORT=1 LZMA_DIR=../../lzma COMP_DEFAULT=lzma

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
cd squashfs-tools
install -m 755 mksquashfs unsquashfs %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
