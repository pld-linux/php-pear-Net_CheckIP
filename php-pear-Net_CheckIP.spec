%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	CheckIP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - check the syntax of IPv4 adresses
Summary(pl.UTF-8):   %{_pearname} - sprawdzanie składni adresów IPv4
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	30bd9ad56a971491be6676112bf294ed
URL:		http://pear.php.net/package/Net_CheckIP/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package validates IPv4 internet adresses.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy zawarte w tym pakiecie sprawdzają poprawność adresów IPv4.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
