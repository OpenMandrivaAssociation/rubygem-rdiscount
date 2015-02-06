# Generated from rdiscount-1.6.8.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	rdiscount

Summary:	Fast Implementation of Gruber's Markdown in C
Name:		rubygem-%{rbname}

Version:	1.6.8
Release:	2
Group:		Development/Ruby
License:	BSD
URL:		http://github.com/rtomayko/rdiscount
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(rake)

%description
Fast Implementation of Gruber's Markdown in C

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(man|test)/'

%install
%gem_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/rdiscount
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rdiscount
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/man
%{ruby_gemdir}/gems/%{rbname}-%{version}/man/*.1
%{ruby_gemdir}/gems/%{rbname}-%{version}/man/*.7
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/COPYING
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
%{ruby_gemdir}/gems/%{rbname}-%{version}/man/*.ronn
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.txt


%changelog
* Tue Mar 15 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.6.8-1
+ Revision: 645129
- regenerate spec with gem2rpm5
- new release: 1.6.8

* Sat Dec 04 2010 Rémy Clouard <shikamaru@mandriva.org> 1.6.5-1mdv2011.0
+ Revision: 609256
- add conflicts
- import rubygem-rdiscount

