Summary:	Fast Implementation of Gruber's Markdown in C
Name:		rubygem-rdiscount
Version:	2.2.0.2
Release:	2
Group:		Development/Ruby
License:	BSD
URL:		http://github.com/davidfstr/rdiscount
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	ruby-devel

%description
Fast Implementation of Gruber's Markdown in C

%prep
%autosetup -p1 -n %{gem_name}-%{version}
 
%build
%gem_build 

%install
%gem_install

%files
%{_bindir}/rdiscount
%{gem_files}
