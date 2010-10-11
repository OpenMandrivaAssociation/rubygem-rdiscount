%define oname rdiscount

Summary:    Fast Implementation of Gruber's Markdown in C
Name:       rubygem-%{oname}
Version:    1.6.5
Release:    %mkrel 1
Group:      Development/Ruby
License:    BSD
URL:        http://github.com/rtomayko/rdiscount
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildRequires: ruby-devel
Provides:   rubygem(%{oname}) = %{version}

%description
Fast Implementation of Gruber's Markdown in C

%prep
%setup -q -c

%build
mkdir -p .%{ruby_gemdir}
gem install -V --local --install-dir $PWD/%{ruby_gemdir} \
               --force --rdoc %{SOURCE0}

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
cp -a .%{ruby_gemdir}/* %{buildroot}%{ruby_gemdir}
rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext/

# install the so file in sitearchdir
mkdir -p %{buildroot}%{ruby_sitearchdir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/rdiscount.so %{buildroot}%{ruby_sitearchdir}

# install the manpages
mkdir -p %{buildroot}%{_mandir}/man{1,7}/
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man/%{oname}.1* %{buildroot}%{_mandir}/man1/
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man/markdown.7* %{buildroot}%{_mandir}/man7/

# install executables
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/rdiscount
%{_mandir}/man1/%{oname}.1.*
%{_mandir}/man7/markdown.7.*
%{ruby_sitearchdir}/%{oname}.so
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/rdiscount.gemspec
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.markdown
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
