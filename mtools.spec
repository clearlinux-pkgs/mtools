#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mtools
Version  : 4.0.23
Release  : 4
URL      : ftp://ftp.gnu.org/gnu/mtools/mtools-4.0.23.tar.gz
Source0  : ftp://ftp.gnu.org/gnu/mtools/mtools-4.0.23.tar.gz
Summary  : mtools, read/write/list/format DOS disks under Unix
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: mtools-bin = %{version}-%{release}
Requires: mtools-license = %{version}-%{release}
Requires: mtools-man = %{version}-%{release}
BuildRequires : texinfo

%description
Mtools is a collection of utilities to access MS-DOS disks from GNU
and Unix without mounting them. It supports long file names, OS/2 Xdf
disks, ZIP/JAZ disks and 2m disks (store up to 1992k on a high density
3 1/2 disk).

%package bin
Summary: bin components for the mtools package.
Group: Binaries
Requires: mtools-license = %{version}-%{release}

%description bin
bin components for the mtools package.


%package doc
Summary: doc components for the mtools package.
Group: Documentation
Requires: mtools-man = %{version}-%{release}

%description doc
doc components for the mtools package.


%package license
Summary: license components for the mtools package.
Group: Default

%description license
license components for the mtools package.


%package man
Summary: man components for the mtools package.
Group: Default

%description man
man components for the mtools package.


%prep
%setup -q -n mtools-4.0.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559065544
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1559065544
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mtools
cp COPYING %{buildroot}/usr/share/package-licenses/mtools/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/amuFormat.sh
/usr/bin/lz
/usr/bin/mattrib
/usr/bin/mbadblocks
/usr/bin/mcat
/usr/bin/mcd
/usr/bin/mcheck
/usr/bin/mclasserase
/usr/bin/mcomp
/usr/bin/mcopy
/usr/bin/mdel
/usr/bin/mdeltree
/usr/bin/mdir
/usr/bin/mdu
/usr/bin/mformat
/usr/bin/minfo
/usr/bin/mkmanifest
/usr/bin/mlabel
/usr/bin/mmd
/usr/bin/mmount
/usr/bin/mmove
/usr/bin/mpartition
/usr/bin/mrd
/usr/bin/mren
/usr/bin/mshortname
/usr/bin/mshowfat
/usr/bin/mtools
/usr/bin/mtoolstest
/usr/bin/mtype
/usr/bin/mxtar
/usr/bin/mzip
/usr/bin/tgz
/usr/bin/uz

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mtools/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/floppyd.1
/usr/share/man/man1/floppyd_installtest.1
/usr/share/man/man1/mattrib.1
/usr/share/man/man1/mbadblocks.1
/usr/share/man/man1/mcat.1
/usr/share/man/man1/mcd.1
/usr/share/man/man1/mclasserase.1
/usr/share/man/man1/mcopy.1
/usr/share/man/man1/mdel.1
/usr/share/man/man1/mdeltree.1
/usr/share/man/man1/mdir.1
/usr/share/man/man1/mdu.1
/usr/share/man/man1/mformat.1
/usr/share/man/man1/minfo.1
/usr/share/man/man1/mkmanifest.1
/usr/share/man/man1/mlabel.1
/usr/share/man/man1/mmd.1
/usr/share/man/man1/mmount.1
/usr/share/man/man1/mmove.1
/usr/share/man/man1/mpartition.1
/usr/share/man/man1/mrd.1
/usr/share/man/man1/mren.1
/usr/share/man/man1/mshortname.1
/usr/share/man/man1/mshowfat.1
/usr/share/man/man1/mtools.1
/usr/share/man/man1/mtoolstest.1
/usr/share/man/man1/mtype.1
/usr/share/man/man1/mzip.1
/usr/share/man/man5/mtools.5
