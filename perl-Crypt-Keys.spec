#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Keys
Summary:	Crypt::Keys Perl module - public and private key management
Summary(pl.UTF-8):	Moduł Perla Crypt::Keys - zarządzający kluczami publicznymi i prywatnymi
Name:		perl-Crypt-Keys
Version:	0.06
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6c375a9d965ff86d3ae967b9e6bbaf36
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Convert-PEM >= 0.05
BuildRequires:	perl-Crypt-CBC >= 2.00
BuildRequires:	perl-Crypt-DES
BuildRequires:	perl-Data-Buffer
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Math-Pari >= 2.001804
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Convert-PEM >= 0.05
Requires:	perl-Crypt-CBC >= 2.00
Requires:	perl-Math-Pari >= 2.001804
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Keys is an on-disk key management system for public and private
keyfiles. The goal of the module is to be able to read and write
crypto keys in any encoding (eg. PEM, SSH, etc.). It can be used as a
front-end for key management, but it does not contain implementations
of any of the assymetric cryptography algorithms represented by the
keys that it manages. In other words, you can use it to read and write
your DSA/RSA/etc. keys, but it does not generate new keys or
encrypt/sign data.

%description -l pl.UTF-8
Crypt::Keys to system do zarządzania kluczami publicznymi i prywatnymi
przechowywanymi na dysku. Celem tego modułu jest umożliwienie odczytu
i zapisu kluczy kryptograficznych o dowolnym kodowaniu (PEM, SSH
itd.). Może być używany jako interfejs do zarządzania kluczami, ale
nie zawiera implementacji żadnego algorytmu kryptograficznego
reprezentowanego przez klucze, którymi zarządza. Innymi słowy, potrafi
odczytywać i zapisywać klucze DSA/RSA/itp., ale nie jest w stanie
wygenerować nowych kluczy ani odszyfrować czy zaszyfrować danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	< /dev/null
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/Crypt/Keys.pm
%{perl_vendorlib}/Crypt/Keys
%{_mandir}/man3/*
