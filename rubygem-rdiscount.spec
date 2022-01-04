%define gem_name rdiscount

Summary:	Fast Implementation of Gruber's Markdown in C
Name:		rubygem-%{gem_name}

Version:	2.2.0.2
Release:	1
Group:		Development/Ruby
License:	BSD
URL:		http://github.com/davidfstr/rdiscount
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:	ruby-devel

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

%autosetup -n %{gem_name}-%{version}
 
%build
%gem_build 

%install
cp -r %{_builddir}/%{gem_name}-%{version}/usr  %{buildroot}

%files
%{_bindir}/rdiscount
%{_libdir}/ruby/gems/*/specifications/%{gem_name}-%{version}.gemspec
%{_libdir}/ruby/gems/*/cache/%{gem_name}-%{version}.gem
%{_libdir}/ruby/gems/*/gems/%{gem_name}-%{version}
%{_libdir}/ruby/gems/*/extensions/*/*/%{gem_name}-%{version}


%files doc
%doc %{_libdir}/ruby/gems/*/doc/%{gem_name}-* 
