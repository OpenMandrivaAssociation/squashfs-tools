%define sqname	squashfs
%define sqver	4.0
%define cvsdate 20091221
%define release	%mkrel 3.%cvsdate.1
%define	Summary	Utilities for the creation of compressed squashfs images

Name:		%{sqname}-tools
Version:	%{sqver}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}-%{cvsdate}.tar.gz
Source1:	lzma465.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -T -c -b1 -n lzma
%setup -q -n %{sqname}-%{cvsdate}

%build
%make LZMA_SUPPORT=1 LZMA_DIR=../lzma/

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 mksquashfs unsquashfs %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
