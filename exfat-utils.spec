Summary:	Utilities for exFAT filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików exFAT
Name:		exfat-utils
Version:	1.1.1
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: http://code.google.com/p/exfat/downloads/list
#Source0:	http://exfat.googlecode.com/files/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6f0a276bbfdcdd8c94ac2f72625cc7c9
URL:		http://code.google.com/p/exfat/
BuildRequires:	rpmbuild(macros) >= 1.385
BuildRequires:	scons
Suggests:	fuse-exfat
Conflicts:	fuse-exfat < 0.9.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
export CFLAGS="%{rpmcflags} -std=c99"
%scons

%install
rm -rf $RPM_BUILD_ROOT
export CFLAGS="%{rpmcflags} -std=c99"
%scons install \
	DESTDIR=$RPM_BUILD_ROOT/sbin

install -d $RPM_BUILD_ROOT%{_mandir}/man8
cp -p dump/dumpexfat.8 \
	fsck/exfatfsck.8 \
	label/exfatlabel.8 \
	mkfs/mkexfatfs.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo '.so man8/exfatfsck.8' >$RPM_BUILD_ROOT%{_mandir}/man8/fsck.exfat.8
echo '.so man8/mkexfatfs.8' >$RPM_BUILD_ROOT%{_mandir}/man8/mkfs.exfat.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
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
