%define sqname	squashfs
%define sqver	4.0
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{sqname}%{sqver}

%build
%make -C %{name} 

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 %{name}/mksquashfs %{name}/unsquashfs %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/mksquashfs
%{_bindir}/unsquashfs
