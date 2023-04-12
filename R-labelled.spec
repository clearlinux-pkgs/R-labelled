#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-labelled
Version  : 2.11.0
Release  : 67
URL      : https://cran.r-project.org/src/contrib/labelled_2.11.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/labelled_2.11.0.tar.gz
Summary  : Manipulating Labelled Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-dplyr
Requires: R-haven
Requires: R-lifecycle
Requires: R-rlang
Requires: R-stringr
Requires: R-tidyr
Requires: R-vctrs
BuildRequires : R-dplyr
BuildRequires : R-haven
BuildRequires : R-lifecycle
BuildRequires : R-memisc
BuildRequires : R-rlang
BuildRequires : R-stringr
BuildRequires : R-tidyr
BuildRequires : R-vctrs
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
or 'Stata' with 'haven' or 'foreign'. This package
    provides useful functions to deal with "haven_labelled" and
    "haven_labelled_spss" classes introduced by 'haven' package.

%prep
%setup -q -n labelled

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681317397

%install
export SOURCE_DATE_EPOCH=1681317397
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/labelled/DESCRIPTION
/usr/lib64/R/library/labelled/INDEX
/usr/lib64/R/library/labelled/Meta/Rd.rds
/usr/lib64/R/library/labelled/Meta/data.rds
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
/usr/lib64/R/library/labelled/WORDLIST
/usr/lib64/R/library/labelled/data/Rdata.rdb
/usr/lib64/R/library/labelled/data/Rdata.rds
/usr/lib64/R/library/labelled/data/Rdata.rdx
/usr/lib64/R/library/labelled/doc/index.html
/usr/lib64/R/library/labelled/doc/intro_labelled.R
/usr/lib64/R/library/labelled/doc/intro_labelled.Rmd
/usr/lib64/R/library/labelled/doc/intro_labelled.html
/usr/lib64/R/library/labelled/doc/look_for.R
/usr/lib64/R/library/labelled/doc/look_for.Rmd
/usr/lib64/R/library/labelled/doc/look_for.html
/usr/lib64/R/library/labelled/doc/missing_values.R
/usr/lib64/R/library/labelled/doc/missing_values.Rmd
/usr/lib64/R/library/labelled/doc/missing_values.html
/usr/lib64/R/library/labelled/help/AnIndex
/usr/lib64/R/library/labelled/help/aliases.rds
/usr/lib64/R/library/labelled/help/figures/labelled.png
/usr/lib64/R/library/labelled/help/figures/labelled.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/labelled/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/labelled/help/labelled.rdb
/usr/lib64/R/library/labelled/help/labelled.rdx
/usr/lib64/R/library/labelled/help/paths.rds
/usr/lib64/R/library/labelled/html/00Index.html
/usr/lib64/R/library/labelled/html/R.css
/usr/lib64/R/library/labelled/tests/spelling.R
/usr/lib64/R/library/labelled/tests/testthat.R
/usr/lib64/R/library/labelled/tests/testthat/test-copy_labels.r
/usr/lib64/R/library/labelled/tests/testthat/test-labelled.r
/usr/lib64/R/library/labelled/tests/testthat/test-miscellanous.R
/usr/lib64/R/library/labelled/tests/testthat/test-na_values.R
/usr/lib64/R/library/labelled/tests/testthat/test-recode_if.r
/usr/lib64/R/library/labelled/tests/testthat/test-tagged_na.r
/usr/lib64/R/library/labelled/tests/testthat/test-to_labelled.r
/usr/lib64/R/library/labelled/tests/testthat/test_lookfor.R
