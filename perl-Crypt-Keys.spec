%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Keys
Summary:	Crypt::Keys Perl module - public and private key management
Summary(pl):	Modu³ Perla Crypt::Keys - zarz±dzaj±cy kluczami publicznymi i prywatnymi
Name:		perl-Crypt-Keys
Version:	0.06
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
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

%description -l pl
Crypt::Keys to system do zarz±dzania kluczami publicznymi i prywatnymi
przechowywanymi na dysku. Celem tego modu³u jest umo¿liwienie odczytu
i zapisu kluczy kryptograficznych o dowolnym kodowaniu (PEM, SSH
itd.). Mo¿e byæ u¿ywany jako interfejs do zarz±dzania kluczami, ale
nie zawiera implementacji ¿adnego algorytmu kryptograficznego
reprezentowanego przez klucze, którymi zarz±dza. Innymi s³owy, potrafi
odczytywaæ i zapisywaæ klucze DSA/RSA/itp., ale nie jest w stanie
wygenerowaæ nowych kluczy ani odszyfrowaæ czy zaszyfrowaæ danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo 3 | perl Makefile.PL
%{__make}
%{__make} test

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
