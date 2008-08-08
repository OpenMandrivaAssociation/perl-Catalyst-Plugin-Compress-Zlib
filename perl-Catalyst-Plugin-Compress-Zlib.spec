
%define realname   Catalyst-Plugin-Compress-Zlib
%define version    0.03
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Gzip response
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Compress::Zlib)

BuildArch: noarch

%description
Gzip compress response if client supports it.




%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc META.yml README Changes
%{_mandir}/man3/*
%perl_vendorlib/*



