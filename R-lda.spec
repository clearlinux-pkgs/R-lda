#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-lda
Version  : 1.4.2
Release  : 11
URL      : https://cran.r-project.org/src/contrib/lda_1.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/lda_1.4.2.tar.gz
Summary  : Collapsed Gibbs Sampling Methods for Topic Models
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-lda-lib
BuildRequires : clr-R-helpers

%description
and related models.  This includes (but is not limited
	     to) sLDA, corrLDA, and the mixed-membership stochastic
	     blockmodel.  Inference for all of these models is
	     implemented via a fast collapsed Gibbs sampler written
	     in C.  Utility functions for reading/writing data
	     typically used in topic models, as well as tools for
	     examining posterior distributions are also included.

%package lib
Summary: lib components for the R-lda package.
Group: Libraries

%description lib
lib components for the R-lda package.


%prep
%setup -q -c -n lda

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523312962

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523312962
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lda
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library lda
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library lda|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/lda/DESCRIPTION
/usr/lib64/R/library/lda/INDEX
/usr/lib64/R/library/lda/Meta/Rd.rds
/usr/lib64/R/library/lda/Meta/data.rds
/usr/lib64/R/library/lda/Meta/demo.rds
/usr/lib64/R/library/lda/Meta/features.rds
/usr/lib64/R/library/lda/Meta/hsearch.rds
/usr/lib64/R/library/lda/Meta/links.rds
/usr/lib64/R/library/lda/Meta/nsInfo.rds
/usr/lib64/R/library/lda/Meta/package.rds
/usr/lib64/R/library/lda/NAMESPACE
/usr/lib64/R/library/lda/R/lda
/usr/lib64/R/library/lda/R/lda.rdb
/usr/lib64/R/library/lda/R/lda.rdx
/usr/lib64/R/library/lda/data/cora.cites.rda
/usr/lib64/R/library/lda/data/cora.documents.rda
/usr/lib64/R/library/lda/data/cora.titles.rda
/usr/lib64/R/library/lda/data/cora.vocab.rda
/usr/lib64/R/library/lda/data/datalist
/usr/lib64/R/library/lda/data/newsgroup.label.map.rda
/usr/lib64/R/library/lda/data/newsgroup.test.documents.rda
/usr/lib64/R/library/lda/data/newsgroup.test.labels.rda
/usr/lib64/R/library/lda/data/newsgroup.train.documents.rda
/usr/lib64/R/library/lda/data/newsgroup.train.labels.rda
/usr/lib64/R/library/lda/data/newsgroup.vocab.rda
/usr/lib64/R/library/lda/data/poliblog.documents.rda
/usr/lib64/R/library/lda/data/poliblog.ratings.rda
/usr/lib64/R/library/lda/data/poliblog.vocab.rda
/usr/lib64/R/library/lda/data/sampson.rda
/usr/lib64/R/library/lda/demo/lda.R
/usr/lib64/R/library/lda/demo/mmsb.R
/usr/lib64/R/library/lda/demo/nubbi.R
/usr/lib64/R/library/lda/demo/rtm.R
/usr/lib64/R/library/lda/demo/slda.R
/usr/lib64/R/library/lda/demo/sldamc.R
/usr/lib64/R/library/lda/help/AnIndex
/usr/lib64/R/library/lda/help/aliases.rds
/usr/lib64/R/library/lda/help/lda.rdb
/usr/lib64/R/library/lda/help/lda.rdx
/usr/lib64/R/library/lda/help/paths.rds
/usr/lib64/R/library/lda/html/00Index.html
/usr/lib64/R/library/lda/html/R.css
/usr/lib64/R/library/lda/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/lda/libs/lda.so
/usr/lib64/R/library/lda/libs/lda.so.avx2
/usr/lib64/R/library/lda/libs/lda.so.avx512
