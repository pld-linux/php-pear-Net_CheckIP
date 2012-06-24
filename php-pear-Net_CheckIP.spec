%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       CheckIP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Check the syntax of IPv4 adresses
Summary(pl):	%{_pearname} - Sprawdzanie sk�adni adres�w IPv4
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package validates IPv4 internet adresses.

This class has in PEAR status: %{_status}.

%description -l pl
Klasy zawarte w tym pakiecie sprawdzaj� poprawno�� adres�w IPv4.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
