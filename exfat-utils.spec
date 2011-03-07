Summary:	Utilities for exFAT filesystem
Summary(pl.UTF-8):	Narzędzia do systemu plików exFAT
Name:		exfat-utils
Version:	0.9.4
Release:	1
License:	GPL v3+
Group:		Applications/System
#Source0Download: http://code.google.com/p/exfat/downloads/list
Source0:	http://exfat.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	678ad6e34e99464087b829a37acfa7b0
URL:		http://code.google.com/p/exfat/
BuildRequires:	rpmbuild(macros) >= 1.385
BuildRequires:	scons
BuildRequires:	sed >= 4.0
Conflicts:	fuse-exfat < 0.9.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide a full-featured exFAT file system
implementation for Linux and other Unix-like systems as a FUSE module.

Current status of the project is beta.

%description -l pl.UTF-8
Celem tego projektu jest umożliwienie pełnego dostępu do systemu
plików exFAT z poziomu Linuksa i innych systemów uniksowych poprzez
moduł FUSE.

Obecny status tego projektu to beta.

%prep
%setup -q

# libfuse not used in -utils
sed -i -e "s/, 'fuse'//" SConstruct

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT

%scons install \
	DESTDIR=$RPM_BUILD_ROOT/sbin

install -d $RPM_BUILD_ROOT%{_mandir}/man8
install dump/dumpexfat.8 \
	fsck/exfatfsck.8 \
	label/exfatlabel.8 \
	mkfs/mkexfatfs.8 $RPM_BUILD_ROOT%{_mandir}/man8
echo '.so exfatfsck.8' >$RPM_BUILD_ROOT%{_mandir}/man8/fsck.exfat.8
echo '.so mkexfatfs.8' >$RPM_BUILD_ROOT%{_mandir}/man8/mkfs.exfat.8

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
