Name:		fusioninventory-agent-plugin-snmpquery
Version:	1.3
Release:	2
Summary:	OCS Inventory Software deployment support for FusionInventory agent
License:	GPL
Group:		System/Servers
URL:		http://fusioninventory.org/wordpress/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FU/FUSINV/FusionInventory-Agent-Task-SNMPQuery-%{version}.tar.gz
BuildArch:  noarch
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Module::CoreList)
BuildRequires:  perl-devel

%description
With this module, FusionInventory can accept software deployment request from
an OCS Inventory server.

%prep
%setup -q -n FusionInventory-Agent-Task-SNMPQuery-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc AUTHORS Changes README LICENSE
%{perl_vendorlib}/FusionInventory



%changelog
* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdv2011.0
+ Revision: 649134
- update to new version 1.3

* Mon Aug 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2011.0
+ Revision: 570311
- new version

* Mon Aug 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-2mdv2011.0
+ Revision: 564984
- fix backportability

* Mon Aug 02 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2011.0
+ Revision: 564971
- new version

* Mon May 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2010.1
+ Revision: 541802
- import fusioninventory-agent-plugin-snmpquery


* Mon May 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdv2010.1
- initial mdv release
