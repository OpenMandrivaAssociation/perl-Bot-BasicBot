%define upstream_name	 Bot-BasicBot
%define upstream_version 0.87

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A simple IRC bot base class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TO/TOMI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(POE::Component::IRC)
BuildArch:	noarch

%description
A basic bot system written in Perl, designed to make it easy to do simple bots,
optionally forking longer processes (like searches) concurrently in the
background.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# some backup files leaked, removing them
#find . -name "._*" | xargs rm

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests try to connect to internet
#%make test

%install
%makeinstall_std

%files
%doc Changes examples
%{perl_vendorlib}/Bot/*
%{_mandir}/*/*

%changelog
* Sun May 15 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.870.0-1mdv2011.0
+ Revision: 674794
- update to new version 0.87

* Mon Apr 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.860.0-1
+ Revision: 650278
- update to new version 0.86

* Tue Nov 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.840.0-1mdv2011.0
+ Revision: 598066
- update to new version 0.84

* Sat Nov 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.830.0-1mdv2011.0
+ Revision: 597213
- update to 0.83

* Tue Jul 07 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.810.0-1mdv2011.0
+ Revision: 393093
- update to 0.81
- using %%perl_convert_version
- sanitizing spec file

* Fri Jan 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.81-1mdv2009.1
+ Revision: 335552
- update to new version 0.81

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.70-6mdv2009.0
+ Revision: 255469
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.70-4mdv2008.1
+ Revision: 136664
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.70-4mdv2007.0
+ Revision: 108605
- really fix version
- fix release
- rebuild

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.7-1mdv2007.0
+ Revision: 53709
- 0.7
- Import perl-Bot-BasicBot

* Tue Oct 11 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.65-3mdk
- Fix BuildRequires

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.65-2mdk
- Buildrequires fix

* Tue Aug 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.65-1mdk
- 0.65

* Wed May 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.61-1mdk
- 0.61

* Fri Apr 01 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.6-1mdk
- 0.6

* Sun Feb 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.5-1mdk
- Initial MDK release.

