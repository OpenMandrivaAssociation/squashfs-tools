%define sqname	squashfs
%define sqver	4.0
%define cvsdate 20090125
%define release	%mkrel 0.%cvsdate.1
%define	Summary	Utilities for the creation of compressed squashfs images

Name:		%{sqname}-tools
Version:	%{sqver}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		File tools
URL:		http://squashfs.sourceforge.net/
Source0:	%{sqname}-%{cvsdate}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel

%description
squashfs-tools are utilities for the creation of compressed squashfs images.

%prep
%setup -q -n %{sqname}

%build
%make -C %{name} 

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 %{name}/mksquashfs %{buildroot}%{_bindir}
# %{name}/unsquashfs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/mksquashfs
#%{_bindir}/unsquashfs
