#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-python_language_server
Version  : 0.36.2
Release  : 34
URL      : https://files.pythonhosted.org/packages/66/30/0c31b052ede62bbeddf4110db57c78d3c704506178caa18b2f0be2271293/python-language-server-0.36.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/30/0c31b052ede62bbeddf4110db57c78d3c704506178caa18b2f0be2271293/python-language-server-0.36.2.tar.gz
Summary  : Python Language Server for the Language Server Protocol
Group    : Development/Tools
License  : MIT
Requires: pypi-python_language_server-bin = %{version}-%{release}
Requires: pypi-python_language_server-license = %{version}-%{release}
Requires: pypi-python_language_server-python = %{version}-%{release}
Requires: pypi-python_language_server-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jedi)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(python_jsonrpc_server)
BuildRequires : pypi(ujson)
Patch1: deps.patch

%description
======================

%package bin
Summary: bin components for the pypi-python_language_server package.
Group: Binaries
Requires: pypi-python_language_server-license = %{version}-%{release}

%description bin
bin components for the pypi-python_language_server package.


%package license
Summary: license components for the pypi-python_language_server package.
Group: Default

%description license
license components for the pypi-python_language_server package.


%package python
Summary: python components for the pypi-python_language_server package.
Group: Default
Requires: pypi-python_language_server-python3 = %{version}-%{release}

%description python
python components for the pypi-python_language_server package.


%package python3
Summary: python3 components for the pypi-python_language_server package.
Group: Default
Requires: python3-core
Provides: pypi(python_language_server)
Requires: pypi(jedi)
Requires: pypi(pluggy)
Requires: pypi(python_jsonrpc_server)
Requires: pypi(ujson)

%description python3
python3 components for the pypi-python_language_server package.


%prep
%setup -q -n python-language-server-0.36.2
cd %{_builddir}/python-language-server-0.36.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651101790
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-python_language_server
cp %{_builddir}/python-language-server-0.36.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-python_language_server/4df3c87108ebab83aa7bb222e245d841c6574d4f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyls

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-python_language_server/4df3c87108ebab83aa7bb222e245d841c6574d4f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
