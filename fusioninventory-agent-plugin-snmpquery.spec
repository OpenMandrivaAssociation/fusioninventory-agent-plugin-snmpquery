Name:		fusioninventory-agent-plugin-snmpquery
Version:	1.0
Release:	%mkrel 1
Summary:	OCS Inventory Software deployment support for FusionInventory agent
License:	GPL
Group:		System/Servers
URL:		http://fusioninventory.org/wordpress/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GO/GONERI/FusionInventory-Agent-Task-SNMPQuery-%{version}.tar.gz
BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
With this module, FusionInventory can accept software deployment request from
an OCS Inventory server.

%prep
%setup -q -n FusionInventory-Agent-Task-SNMPQuery-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf  %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changes README LICENSE
%{perl_vendorlib}/FusionInventory

