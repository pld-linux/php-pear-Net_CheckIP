%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       CheckIP
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Check the syntax of IPv4 adresses
Summary(pl):	%{_class}_%{_subclass} - Sprawdzanie sk³adni adresów IPv4
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package validates IPv4 internet adresses.

%description -l pl
Klasy zawarte w tym pakiecie sprawdzaj± poprawno¶æ adresów IPv4.

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
