%global _python_bytecompile_extra 0
%global module pyqtgraph

Name:		python-pyqtgraph
Version:	0.14.0
Release:	1
Summary:	Scientific Graphics and GUI Library for Python
License:	MIT
URL:		https://www.pyqtgraph.org/
Source0:	https://github.com/pyqtgraph/pyqtgraph/archive/%{module}-%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pyopengl)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python-qt6-devel
Requires:	python-qt6
Suggests:	%{name}-doc = %{version}-%{release}

%global _description %{expand:
PyQtGraph is a pure-python graphics and GUI library built on PyQt4 / PySide and
numpy. It is intended for use in mathematics / scientific /engineering
applications. Despite being written entirely in python, the library is very
fast due to its heavy leverage of numpy for number crunching and Qt\'s
GraphicsView framework for fast display.}

%description %_description

%package doc
Summary:	Documentation for the %{module} library

%description doc
This package provides examples and documentation
for the %{module} library.

%prep -a
# Fix rpmlint warnings
chmod a-x pyqtgraph/examples/Symbols.py
# Some example scripts have interpreters decalred, remove all as they don't have executable bits
sed -i '1{/^#!/ d}' pyqtgraph/examples/*.py
# Fix EOL
sed -i 's/\r//' pyqtgraph/examples/DateAxisItem_QtDesigner.ui
# gcc calls, but not properly marked as script
chmod -x pyqtgraph/examples/verlet_chain/make

%install -a
#rm -rf %{buildroot}%{python_sitelib}/pyqtgraph/examples
rm -f doc/build/html/.buildinfo
rm -f doc/build/html/objects.inv
# mkdir and copy exmples into buildroot/docdir
mkdir -p %{buildroot}%{_docdir}/%{name}/
#cp -r pyqtgraph/examples %{buildroot}%{_docdir}/%{name}/
mv -f %{buildroot}%{python_sitelib}/pyqtgraph/examples %{buildroot}%{_docdir}/%{name}/

%files
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

%files doc
%{_docdir}/%{name}/examples
