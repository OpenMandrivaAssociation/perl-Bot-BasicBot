%define upstream_name	 Bot-BasicBot
%define upstream_version 0.87

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A simple IRC bot base class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/T/TO/TOMI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POE::Component::IRC)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
A basic bot system written in Perl, designed to make it easy to do simple bots,
optionally forking longer processes (like searches) concurrently in the
background.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# some backup files leaked, removing them
#find . -name "._*" | xargs rm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests try to connect to internet
#%make test

%install
rm -rf %{buildroot}
%{makeinstall_std}

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes examples
%{perl_vendorlib}/Bot/*
%{_mandir}/*/*

