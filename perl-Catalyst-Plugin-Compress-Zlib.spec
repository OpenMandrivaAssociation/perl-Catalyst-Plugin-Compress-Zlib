%define upstream_name    Catalyst-Plugin-Compress-Zlib
Name:		perl-%{upstream_name}
Version:	0.06
Release:	5

Summary:	Gzip response
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://dev.catalyst.perl.org/repos/Catalyst/trunk/Catalyst-Plugin-Compress-Zlib
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Catalyst-Plugin-Compress-Zlib-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Compress::Zlib)
BuildArch:	noarch

%description
Gzip compress response if client supports it.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 653554
- rebuild for updated spec-helper

* Thu Jul 29 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 563195
- new version

* Sat Nov 21 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 467875
- update to 0.04

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 402988
- rebuild using %0.06 Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2009.0
+ Revision: 268392
- rebuild early 2009.0 package (before pixel changes)

* Mon May 05 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2009.0
+ Revision: 201214
- fix extra space at top of description

* Thu May 01 2008 Olivier Thauvin <nanardon@mandriva.org> 0.03-1mdv2009.0
+ Revision: 199785
- import perl-Catalyst-Plugin-Compress-Zlib



