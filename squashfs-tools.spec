%define sqname	squashfs
%define sqver	3.2
%define sqrelease r2
%define release	%mkrel 1.%{sqrelease}.2
%define	Summary	Utilities for the creation of compressed squashfs images

Name:		%{sqname}-tools
Version:	%{sqver}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}%{sqver}-%{sqrelease}.tar.bz2
Source1:	sqlzma.h
Source2:	sqmagic.h
Patch0:		sqlzma2u-3.2-r2.patch
Patch1:		squashfs3.2-r2-nolzma.patch
BuildRequires:	lzma-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
%{Summary}

%prep
%setup -q -n %{sqname}%{sqver}-%{sqrelease}
%patch0 -p1 -b .lzma
%patch1 -p1 -b .nolzma
cp %{SOURCE1} %{SOURCE2} %{name}

%build
%make -C %{name} Sqlzma=. LzmaAlone=%{_libdir} LzmaC=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -m 755 %{name}/mksquashfs -D $RPM_BUILD_ROOT%{_bindir}/mksquashfs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ACKNOWLEDGEMENTS CHANGES README
%{_bindir}/mksquashfs


