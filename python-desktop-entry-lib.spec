Name:		python-desktop-entry-lib
Version:	5.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/desktop_entry_lib/desktop_entry_lib-%{version}.tar.gz
Summary:	A library for working with .desktop files
URL:		https://pypi.org/project/desktop-entry-lib/
License:	BSD-2-Clause
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

%description
A library for working with .desktop files

%files
%{py_sitedir}/desktop_entry_lib/*
%{py_sitedir}/desktop_entry_lib-*.*-info
