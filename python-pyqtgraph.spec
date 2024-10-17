%global _python_bytecompile_extra 0
%global srcname pyqtgraph

Name:           python-%{srcname}
Version:        0.13.7
Release:        1
Summary:        Scientific Graphics and GUI Library for Python
License:        MIT
URL:            https://www.pyqtgraph.org/
Source0:	https://files.pythonhosted.org/packages/source/p/pyqtgraph/pyqtgraph-%{version}.tar.gz
# git clone https://github.com/pyqtgraph/test-data
# tar -zcf pyqtgraph-test-data-5498050.tar.gz test-data
#Source1:        pyqtgraph-test-data-5498050.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-numpy
BuildRequires:  python-opengl

%global _description %{expand:
PyQtGraph is a pure-python graphics and GUI library built on PyQt4 / PySide and
numpy. It is intended for use in mathematics / scientific /engineering
applications. Despite being written entirely in python, the library is very
fast due to its heavy leverage of numpy for number crunching and Qt\'s
GraphicsView framework for fast display.}

%description %_description


%package doc
Summary:        Documentation for the %{srcname} library

%description doc
This package provides documentation for the %{srcname} library.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py_build

%install
%py_install
rm -rf %{buildroot}/%{python_sitelib}/pyqtgraph/examples
rm -f doc/build/html/.buildinfo
rm -f doc/build/html/objects.inv

%files
%license LICENSE.txt
%doc CHANGELOG README.md
%{python_sitelib}/*
