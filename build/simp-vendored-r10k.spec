%global pkgname simp-r10k

%global gemdir /usr/share/simp/ruby
%global simp_bindir /usr/share/simp/bin
%global geminstdir %{gemdir}/%{pkgname}-%{version}

%global colored_version 1.2
%global cri_version 2.6.1
%global faraday_version 0.9.2
%global faraday_middleware_version 0.10.1
%global log4r_version 1.1.10
%global minitar_version 0.6.1
%global multipart_post_version 2.0.0
%global multi_json_version 1.12.1
%global puppet_forge_version 2.1.5

%global r10k_version 2.2.2

# gem2ruby's method of installing gems into mocked build roots will blow up
# unless this line is present:
%define _unpackaged_files_terminate_build 0

Summary: A non-conflicting release of r10k
Name: simp-vendored-r10k
Version: %{r10k_version}
Release: 0
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
Source0: %{name}-%{version}-%{release}.tar.gz
Requires: puppet-agent
Requires: %{name}-doc
Requires: rubygem(%{pkgname}-colored) >= %{colored_version}
Requires: rubygem(%{pkgname}-cri) >= %{cri_version}
Requires: rubygem(%{pkgname}-faraday) >= %{faraday_version}
Requires: rubygem(%{pkgname}-faraday_middleware) >= %{faraday_middleware_version}
Requires: rubygem(%{pkgname}-log4r) >= %{log4r_version}
Requires: rubygem(%{pkgname}-minitar) >= %{minitar_version}
Requires: rubygem(%{pkgname}-multipart-post) >= %{multipart_post_version}
Requires: rubygem(%{pkgname}-multi_json) >= %{multi_json}
Requires: rubygem(%{pkgname}-puppet_forge) >= %{puppet_forge}
BuildArch: noarch

%description
A vendored version of r10k designed to prevent conflicts with any other gems on
the system.

You do *not* need to use this package to install r10k. The traditional methods
documented on the Internet, or the version that ships with Puppet Enterprise
will also work.

This was specifically designed for situations where Internet access is
difficult or unattainable.

Binaries from this package will be located at %{simp_binpath} and will not be
in your path by default.

%package doc
Summary: Documentation for the SIMP r10k installation
Version: %{r10k_version}
Release: 0
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
BuildArch: noarch

%description doc

Documentation for the SIMP r10k installation including sample configuration and
postrun scripts suited to a SIMP environment.

%package gem-colored
Summary: A colored Gem for use with %{name}
Version: %{colored_version}
Release: 0
License: MIT
URL: https://github.com/defunkt/colored
Source11: colored-%{colored_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-colored) = %{colored_version}

%description gem-colored

Gem dependency for %{name}

%package gem-cri
Summary: A cri Gem for use with %{name}
Version: %{cri_version}
Release: 0
License: MIT
URL: https://github.com/defunkt/cri
Source12: cri-%{cri_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-cri) = %{cri_version}

%description gem-cri

Gem dependency for %{name}

%package gem-faraday
Summary: A faraday Gem for use with %{name}
Version: %{faraday_version}
Release: 0
License: MIT
URL: https://github.com/lostisland/faraday
Source13: faraday-%{faraday_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday) = %{faraday_version}

%description gem-faraday

Gem dependency for %{name}

%package gem-faraday_middleware
Summary: A faraday_middleware Gem for use with %{name}
Version: %{faraday_middleware_version}
Release: 0
License: MIT
URL: https://github.com/lostisland/faraday_middleware
Source14: faraday_middleware-%{faraday_middleware_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday_middleware) = %{faraday_middleware_version}

%description gem-faraday_middleware

Gem dependency for %{name}

%package gem-log4r
Summary: A log4r Gem for use with %{name}
Version: %{log4r_version}
Release: 0
License: MIT
URL: http://log4r.rubyforge.org/
Source15: log4r-%{log4r_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-log4r) = %{log4r_version}

%description gem-log4r

Gem dependency for %{name}

%package gem-minitar
Summary: A minitar Gem for use with %{name}
Version: %{minitar_version}
Release: 0
License: Ruby
URL: https://github.com/halostatue/minitar/
Source16: minitar-%{minitar_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-minitar) = %{minitar_version}

%description gem-minitar

Gem dependency for %{name}

%package gem-multipart-post
Summary: A multipart-post Gem for use with %{name}
Version: %{multipart_post_version}
Release: 0
License: MIT
URL: https://github.com/nicksieger/multipart-post
Source17: multipart-post-%{multipart_post_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-multipart-post) = %{multipart_post_version}

%description gem-multipart-post

Gem dependency for %{name}

%package gem-multi_json
Summary: A multi_json Gem for use with %{name}
Version: %{multi_json_version}
Release: 0
License: MIT
URL: http://github.com/intridea/multi_json
Source18: multi_json-%{multi_json_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-multi_json) = %{multi_json_version}

%description gem-multi_json

Gem dependency for %{name}

%package gem-puppet_forge
Summary: A puppet_forge Gem for use with %{name}
Version: %{puppet_forge_version}
Release: 0
License: MIT
URL: https://github.com/defunkt/puppet_forge
Source19: puppet_forge-%{puppet_forge_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-puppet_forge) = %{puppet_forge_version}

%description gem-puppet_forge

Gem dependency for %{name}

%package gem-r10k
Summary: A r10k Gem for use with %{name}
Version: %{r10k_version}
Release: 0
License: Apache-2.0
URL: https://github.com/puppetlabs/r10k
Source20: r10k-%{r10k_version}.gem
BuildRequires: ruby(rubygems)
BuildRequires: ruby
BuildArch: noarch
Provides: rubygem(%{pkgname}-r10k) = %{r10k_version}

%description gem-r10k

Gem dependency for %{name}

%prep
%setup -q

%build

%install
echo "======= %setup PWD: ${PWD}"
echo "======= %setup gemdir: %{gemdir}"

mkdir -p %{buildroot}/%{gemdir}
mkdir -p %{buildroot}/%{geminstdir}
mkdir -p %{buildroot}/%{simp_bindir}
mkdir -p %{buildroot}/%{_var}/simp/cache/r10k

%{lua:
  for i=11,20 do
    print("gem install --local --install-dir ")
    print(rpm.expand("%{buildroot}"))
    print("/")
    print(rpm.expand("%{geminstdir}"))
    print(" --force ")
    print(rpm.expand("%{SOURCE"..i.."}\n"))
  end
}

cat <<EOM > %{buildroot}%{simp_bindir}/r10k
#!/bin/bash

export PATH=/opt/puppetlabs/bin:/opt/puppetlabs/puppet/bin:\$PATH
export GEM_PATH=%{geminstdir}:\$GEM_PATH

%{geminstdir}/gems/r10k-%{r10k_version}/bin/r10k \$@
EOM

%files
%defattr(0644, root, root, 0755)
%attr(0755,-,-) %{simp_bindir}/r10k
%dir %attr(0750,-,-) %{_var}/simp/cache/r10k

%files doc
%doc docs/*

%files gem-colored
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/colored-%{colored_version}
%exclude %{geminstdir}/cache/colored-%{colored_version}.gem
%{geminstdir}/specifications/colored-%{colored_version}.gemspec

%files gem-cri
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/cri-%{cri_version}
%exclude %{geminstdir}/cache/cri-%{cri_version}.gem
%{geminstdir}/specifications/cri-%{cri_version}.gemspec

%files gem-faraday
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday-%{faraday_version}
%exclude %{geminstdir}/cache/faraday-%{faraday_version}.gem
%{geminstdir}/specifications/faraday-%{faraday_version}.gemspec

%files gem-faraday_middleware
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday_middleware-%{faraday_middleware_version}
%exclude %{geminstdir}/cache/faraday_middleware-%{faraday_middleware_version}.gem
%{geminstdir}/specifications/faraday_middleware-%{faraday_middleware_version}.gemspec

%files gem-log4r
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/log4r-%{log4r_version}
%exclude %{geminstdir}/cache/log4r-%{log4r_version}.gem
%{geminstdir}/specifications/log4r-%{log4r_version}.gemspec

%files gem-minitar
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/minitar-%{minitar_version}
%exclude %{geminstdir}/cache/minitar-%{minitar_version}.gem
%{geminstdir}/specifications/minitar-%{minitar_version}.gemspec

%files gem-multipart-post
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/multipart-post-%{multipart_post_version}
%exclude %{geminstdir}/cache/multipart-post-%{multipart_post_version}.gem
%{geminstdir}/specifications/multipart-post-%{multipart_post_version}.gemspec

%files gem-multi_json
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/multi_json-%{multi_json_version}
%exclude %{geminstdir}/cache/multi_json-%{multi_json_version}.gem
%{geminstdir}/specifications/multi_json-%{multi_json_version}.gemspec

%files gem-puppet_forge
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/puppet_forge-%{puppet_forge_version}
%exclude %{geminstdir}/cache/puppet_forge-%{puppet_forge_version}.gem
%{geminstdir}/specifications/puppet_forge-%{puppet_forge_version}.gemspec

%files gem-r10k
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/r10k-%{r10k_version}
%attr(0755,-,-) %{geminstdir}/gems/r10k-%{r10k_version}/bin/r10k
%exclude %{geminstdir}/cache/r10k-%{r10k_version}.gem
%{geminstdir}/specifications/r10k-%{r10k_version}.gemspec

%changelog
* Fri Sep 01 2017 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.2.2
- First release of r10k wrapper
