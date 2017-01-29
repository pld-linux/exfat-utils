Summary:	Utilities for exFAT filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików exFAT
Name:		exfat-utils
Version:	1.2.6
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/relan/exfat/releases
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5367f06a1540eecf4f94c2119cdbd924
URL:		https://github.com/relan/exfat
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11.2
Suggests:	fuse-exfat
Conflicts:	fuse-exfat < 0.9.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This project aims to provide a full-featured exFAT file system
implementation for Linux and other Unix-like systems as a FUSE module.

%description -l pl.UTF-8
Celem tego projektu jest umożliwienie pełnego dostępu do systemu
plików exFAT z poziomu Linuksa i innych systemów uniksowych poprzez
moduł FUSE.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so man8/exfatfsck.8' >$RPM_BUILD_ROOT%{_mandir}/man8/fsck.exfat.8
echo '.so man8/mkexfatfs.8' >$RPM_BUILD_ROOT%{_mandir}/man8/mkfs.exfat.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) /sbin/dumpexfat
%attr(755,root,root) /sbin/exfatfsck
%attr(755,root,root) /sbin/exfatlabel
%attr(755,root,root) /sbin/fsck.exfat
%attr(755,root,root) /sbin/mkexfatfs
%attr(755,root,root) /sbin/mkfs.exfat
%{_mandir}/man8/dumpexfat.8*
%{_mandir}/man8/exfatfsck.8*
%{_mandir}/man8/exfatlabel.8*
%{_mandir}/man8/fsck.exfat.8*
%{_mandir}/man8/mkexfatfs.8*
%{_mandir}/man8/mkfs.exfat.8*
