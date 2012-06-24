#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	ES
Summary:	Math::ES - Evolution Strategy Optimizer
Summary(pl):	Math::ES - optymalizacja z u�yciem algorytmu ewolucyjnego
Name:		perl-Math-ES
Version:	0.08
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27202a67acf9d682b8c78905a483b967
BuildRequires:	perl-Math-Random
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package Math::ES provides an object orientated Evolution Strategy
(ES) for function minimization. It supports multiple populations,
elitism, migration, isolation, two selection schemes and self-adapting
step widths.

%description -l pl
Pakiet Math::ES udost�pnia obiektowo zorientowany algorytm ewolucyjny
(ES - Evolution Strategy) do minimalizacji funkcji. Obs�uguje wiele
populacji, elityzm, migracj�, izolacj�, dwa schematy selekcji oraz
samoadaptuj�ce si� d�ugo�ci kroku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

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
%doc Changes README.txt
%{perl_vendorlib}/Math/ES.pm
%{_mandir}/man3/*
