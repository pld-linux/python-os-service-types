#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python library for consuming OpenStack sevice-types-authority data
Summary(pl.UTF-8):	Biblioteka Pythona do konsumowania danych OpenStack sevice-types-authority
Name:		python-os-service-types
Version:	1.7.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/os-service-types/
Source0:	https://files.pythonhosted.org/packages/source/o/os-service-types/os-service-types-%{version}.tar.gz
# Source0-md5:	4a5bc8a60dfb3e98f5e5f975b173c04d
URL:		https://pypi.org/project/os-service-types/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-keystoneauth1 >= 3.4.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-requests-mock >= 1.2.0
BuildRequires:	python-subunit >= 1.0.0
BuildRequires:	python-stestr >= 2.0.0
BuildRequires:	python-testscenarios >= 0.4
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-keystoneauth1 >= 3.4.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-requests-mock >= 1.2.0
BuildRequires:	python3-subunit >= 1.0.0
BuildRequires:	python3-stestr >= 2.0.0
BuildRequires:	python3-testscenarios >= 0.4
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python library for consuming OpenStack sevice-types-authority data.

The "OpenStack Service Types Authority" contains information about
official OpenStack services and their historical service-type aliases.

%description -l pl.UTF-8
Biblioteka Pythona do konsumowania danych OpenStack
sevice-types-authority.

Dane "OpenStack Service Types Authority" zawierają informacje o
oficjalnych usługach OpenStack i ich historycznych aliasach
service-type.

%package -n python3-os-service-types
Summary:	Python library for consuming OpenStack sevice-types-authority data
Summary(pl.UTF-8):	Biblioteka Pythona do konsumowania danych OpenStack sevice-types-authority
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-os-service-types
Python library for consuming OpenStack sevice-types-authority data.

The "OpenStack Service Types Authority" contains information about
official OpenStack services and their historical service-type aliases.

%description -n python3-os-service-types -l pl.UTF-8
Biblioteka Pythona do konsumowania danych OpenStack
sevice-types-authority.

Dane "OpenStack Service Types Authority" zawierają informacje o
oficjalnych usługach OpenStack i ich historycznych aliasach
service-type.

%package apidocs
Summary:	API documentation for Python os-service-types module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona os-service-types
Group:		Documentation

%description apidocs
API documentation for Python os-service-types module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona os-service-types.

%prep
%setup -q -n os-service-types-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/os_service_types
%{py_sitescriptdir}/os_service_types-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-os-service-types
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/os_service_types
%{py3_sitescriptdir}/os_service_types-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,contributor,install,library,reference,*.html,*.js}
%endif
