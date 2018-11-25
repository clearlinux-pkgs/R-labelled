#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-labelled
Version  : 2.0.0
Release  : 16
URL      : https://cran.r-project.org/src/contrib/labelled_2.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/labelled_2.0.0.tar.gz
Summary  : Manipulating Labelled Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-dplyr
Requires: R-haven
Requires: R-memisc
BuildRequires : R-dplyr
BuildRequires : R-haven
BuildRequires : R-memisc
BuildRequires : buildreq-R

%description
or 'Stata' with 'haven' or 'foreign'. This package
    provides useful functions to deal with "haven_labelled" and
    "haven_labelled_spss" classes introduced by 'haven' package.

%prep
%setup -q -c -n labelled

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543136988

%install
export SOURCE_DATE_EPOCH=1543136988
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labelled
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labelled
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labelled
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library labelled|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/labelled/DESCRIPTION
/usr/lib64/R/library/labelled/INDEX
/usr/lib64/R/library/labelled/Meta/Rd.rds
/usr/lib64/R/library/labelled/Meta/features.rds
/usr/lib64/R/library/labelled/Meta/hsearch.rds
/usr/lib64/R/library/labelled/Meta/links.rds
/usr/lib64/R/library/labelled/Meta/nsInfo.rds
/usr/lib64/R/library/labelled/Meta/package.rds
/usr/lib64/R/library/labelled/Meta/vignette.rds
/usr/lib64/R/library/labelled/NAMESPACE
/usr/lib64/R/library/labelled/NEWS.md
/usr/lib64/R/library/labelled/R/labelled
/usr/lib64/R/library/labelled/R/labelled.rdb
/usr/lib64/R/library/labelled/R/labelled.rdx
/usr/lib64/R/library/labelled/doc/index.html
/usr/lib64/R/library/labelled/doc/intro_labelled.R
/usr/lib64/R/library/labelled/doc/intro_labelled.Rmd
/usr/lib64/R/library/labelled/doc/intro_labelled.html
/usr/lib64/R/library/labelled/help/AnIndex
/usr/lib64/R/library/labelled/help/aliases.rds
/usr/lib64/R/library/labelled/help/labelled.rdb
/usr/lib64/R/library/labelled/help/labelled.rdx
/usr/lib64/R/library/labelled/help/paths.rds
/usr/lib64/R/library/labelled/html/00Index.html
/usr/lib64/R/library/labelled/html/R.css
