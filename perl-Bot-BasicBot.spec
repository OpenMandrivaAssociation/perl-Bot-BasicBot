%define module	Bot-BasicBot
%define name	perl-%{module}
%define ver	0.7
%define version 0.81
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A simple IRC bot base class
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOMI/%{module}-%{ver}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl-Module-Build
BuildRequires:  perl-POE-Component-IRC
%description
A basic bot system written in Perl, designed to make it easy to do simple bots,
optionally forking longer processes (like searches) concurrently in the
background.

%prep
%setup -q -n %{module}-%{ver}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README examples
%{perl_vendorlib}/Bot/*
%{_mandir}/*/*



