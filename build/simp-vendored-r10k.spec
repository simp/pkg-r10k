%global pkgname simp-r10k

%global gemdir /usr/share/simp/ruby
%global simp_bindir /usr/share/simp/bin
%global geminstdir %{gemdir}/%{pkgname}

%global r10k_version 3.12.1

# gem2ruby's method of installing gems into mocked build roots will blow up
# unless this line is present:
%define _unpackaged_files_terminate_build 0

Summary: r10k with puppet-safe gem installation
Name: simp-vendored-r10k
Version: %{r10k_version}
Release: 2%{?dist}
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
Source0: %{name}-%{version}-%{release}.tar.gz
%if 0%{?rhel} > 7
Recommends: git
Recommends: puppet-agent
%else
Requires: git
Requires: puppet-agent
%endif
Requires: %{name}-doc
Requires: rubygem(%{pkgname}-r10k) >= %{r10k_version}
Requires: rubygem(%{pkgname}-cri) >= 2.15.10
Requires: rubygem(%{pkgname}-faraday) >= 0.17.4
Requires: rubygem(%{pkgname}-faraday_middleware) >= 0.14.0
Requires: rubygem(%{pkgname}-fast_gettext) >= 1.1.2
Requires: rubygem(%{pkgname}-gettext) >= 3.2.9
Requires: rubygem(%{pkgname}-gettext-setup) >= 0.34
Requires: rubygem(%{pkgname}-locale) >= 2.1.3
Requires: rubygem(%{pkgname}-log4r) >= 1.1.10
Requires: rubygem(%{pkgname}-minitar) >= 0.9
Requires: rubygem(%{pkgname}-multi_json) >= 1.15.0
Requires: rubygem(%{pkgname}-multipart-post) >= 2.1.1
Requires: rubygem(%{pkgname}-puppet_forge) >= 2.3.4
Requires: rubygem(%{pkgname}-r10k) >= 3.12.1
Requires: rubygem(%{pkgname}-semantic_puppet) >= 1.0.4
Requires: rubygem(%{pkgname}-text) >= 1.3.1
Requires: rubygem(%{pkgname}-colored2) >= 3.1.2
Requires: rubygem(%{pkgname}-jwt) >= 2.2.3
BuildArch: noarch

%description
A vendored version of r10k designed to prevent conflicts with any other gems on
the system.

You do *not* need to use this package to install r10k. The traditional methods
documented on the Internet, or the version that ships with Puppet Enterprise
will also work.

This was specifically designed for situations where Internet access is
difficult or unattainable.

Binaries from this package will be located at %{simp_bindir} and will not be
in your path by default.

%package doc
Summary: Documentation for the SIMP r10k installation
Version: %{r10k_version}
Release: 2%{?dist}
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
BuildArch: noarch

%description doc

Documentation for the SIMP r10k installation including sample configuration and
postrun scripts suited to a SIMP environment.

%package gem-cri
Summary: A cri Gem for use with %{name}
Version: 2.15.10
Release: 1%{?dist}
License: MIT
URL: https://github.com/ddfreyne/cri
Source11: cri-2.15.10.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-cri) = 2.15.10

%description gem-cri

Gem dependency for %{name}

%package gem-faraday
Summary: A faraday Gem for use with %{name}
Version: 0.17.4
Release: 1%{?dist}
License: MIT
URL: https://lostisland.github.io/faraday
Source12: faraday-0.17.4.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday) = 0.17.4

%description gem-faraday

Gem dependency for %{name}

%package gem-faraday_middleware
Summary: A faraday_middleware Gem for use with %{name}
Version: 0.14.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/lostisland/faraday_middleware
Source13: faraday_middleware-0.14.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday_middleware) = 0.14.0

%description gem-faraday_middleware

Gem dependency for %{name}

%package gem-fast_gettext
Summary: A fast_gettext Gem for use with %{name}
Version: 1.1.2
Release: 4%{?dist}
License: MIT or Ruby
URL: http://github.com/grosser/fast_gettext
Source14: fast_gettext-1.1.2.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-fast_gettext) = 1.1.2

%description gem-fast_gettext

Gem dependency for %{name}

%package gem-gettext
Summary: A gettext Gem for use with %{name}
Version: 3.2.9
Release: 4%{?dist}
License: Ruby or LGPLv3+
URL: http://ruby-gettext.github.com/
Source15: gettext-3.2.9.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-gettext) = 3.2.9

%description gem-gettext

Gem dependency for %{name}

%package gem-gettext-setup
Summary: A gettext-setup Gem for use with %{name}
Version: 0.34
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/gettext-setup-gem
Source16: gettext-setup-0.34.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-gettext-setup) = 0.34

%description gem-gettext-setup

Gem dependency for %{name}

%package gem-locale
Summary: A locale Gem for use with %{name}
Version: 2.1.3
Release: 1%{?dist}
License: Ruby or LGPLv3+
URL: https://github.com/ruby-gettext/locale
Source17: locale-2.1.3.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-locale) = 2.1.3

%description gem-locale

Gem dependency for %{name}

%package gem-log4r
Summary: A log4r Gem for use with %{name}
Version: 1.1.10
Release: 5%{?dist}
License: MIT
URL: http://log4r.rubyforge.org
Source18: log4r-1.1.10.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-log4r) = 1.1.10

%description gem-log4r

Gem dependency for %{name}

%package gem-minitar
Summary: A minitar Gem for use with %{name}
Version: 0.9
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/halostatue/minitar/
Source19: minitar-0.9.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-minitar) = 0.9

%description gem-minitar

Gem dependency for %{name}

%package gem-multi_json
Summary: A multi_json Gem for use with %{name}
Version: 1.15.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/intridea/multi_json
Source20: multi_json-1.15.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-multi_json) = 1.15.0

%description gem-multi_json

Gem dependency for %{name}

%package gem-multipart-post
Summary: A multipart-post Gem for use with %{name}
Version: 2.1.1
Release: 3%{?dist}
License: MIT
URL: https://github.com/nicksieger/multipart-post
Source21: multipart-post-2.1.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-multipart-post) = 2.1.1

%description gem-multipart-post

Gem dependency for %{name}

%package gem-puppet_forge
Summary: A puppet_forge Gem for use with %{name}
Version: 2.3.4
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/forge-ruby
Source22: puppet_forge-2.3.4.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-puppet_forge) = 2.3.4

%description gem-puppet_forge

Gem dependency for %{name}

%package gem-r10k
Summary: A r10k Gem for use with %{name}
Version: 3.12.1
Release: 2%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/r10k
Source23: r10k-3.12.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-r10k) = 3.12.1

%description gem-r10k

Gem dependency for %{name}

%package gem-semantic_puppet
Summary: A semantic_puppet Gem for use with %{name}
Version: 1.0.4
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/semantic_puppet
Source24: semantic_puppet-1.0.4.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-semantic_puppet) = 1.0.4

%description gem-semantic_puppet

Gem dependency for %{name}

%package gem-text
Summary: A text Gem for use with %{name}
Version: 1.3.1
Release: 4%{?dist}
License: MIT
URL: http://github.com/threedaymonk/text
Source25: text-1.3.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-text) = 1.3.1

%description gem-text

Gem dependency for %{name}

%package gem-colored2
Summary: A colored2 Gem for use with %{name}
Version: 3.1.2
Release: 1%{?dist}
License: MIT
URL: http://github.com/kigster/colored2
Source26: colored2-3.1.2.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-colored2) = 3.1.2

%description gem-colored2

Gem dependency for %{name}

%package gem-jwt
Summary: A jwt Gem for use with %{name}
Version: 2.2.3
Release: 1%{?dist}
License: MIT
URL: https://github.com/jwt/ruby-jwt
Source27: jwt-2.2.3.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-jwt) = 2.2.3

%description gem-jwt

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
  for i=11,27 do
    print("gem install --local --env-shebang --no-user-install --install-dir ")
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


%files gem-cri
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/cri-2.15.10
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/cri-2.15.10.gem
%{geminstdir}/specifications/cri-2.15.10.gemspec

%files gem-faraday
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday-0.17.4
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/faraday-0.17.4.gem
%{geminstdir}/specifications/faraday-0.17.4.gemspec

%files gem-faraday_middleware
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday_middleware-0.14.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/faraday_middleware-0.14.0.gem
%{geminstdir}/specifications/faraday_middleware-0.14.0.gemspec

%files gem-fast_gettext
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/fast_gettext-1.1.2
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/fast_gettext-1.1.2.gem
%{geminstdir}/specifications/fast_gettext-1.1.2.gemspec

%files gem-gettext
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/gettext-3.2.9
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/gettext-3.2.9.gem
%exclude %{geminstdir}/gems/gettext-3.2.9/samples
%{geminstdir}/specifications/gettext-3.2.9.gemspec

%files gem-gettext-setup
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/gettext-setup-0.34
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/gettext-setup-0.34.gem
%{geminstdir}/specifications/gettext-setup-0.34.gemspec

%files gem-locale
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/locale-2.1.3
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/locale-2.1.3.gem
%{geminstdir}/specifications/locale-2.1.3.gemspec

%files gem-log4r
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/log4r-1.1.10
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/log4r-1.1.10.gem
%{geminstdir}/specifications/log4r-1.1.10.gemspec

%files gem-minitar
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/minitar-0.9
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/minitar-0.9.gem
%{geminstdir}/specifications/minitar-0.9.gemspec

%files gem-multi_json
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/multi_json-1.15.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/multi_json-1.15.0.gem
%{geminstdir}/specifications/multi_json-1.15.0.gemspec

%files gem-multipart-post
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/multipart-post-2.1.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/multipart-post-2.1.1.gem
%{geminstdir}/specifications/multipart-post-2.1.1.gemspec

%files gem-puppet_forge
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/puppet_forge-2.3.4
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/puppet_forge-2.3.4.gem
%{geminstdir}/specifications/puppet_forge-2.3.4.gemspec

%files gem-r10k
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/r10k-3.12.1
%attr(0755,-,-) %{geminstdir}/gems/r10k-3.12.1/bin/r10k
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/r10k-3.12.1.gem
%{geminstdir}/specifications/r10k-3.12.1.gemspec

%files gem-semantic_puppet
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/semantic_puppet-1.0.4
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/semantic_puppet-1.0.4.gem
%{geminstdir}/specifications/semantic_puppet-1.0.4.gemspec

%files gem-text
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/text-1.3.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/text-1.3.1.gem
%{geminstdir}/specifications/text-1.3.1.gemspec

%files gem-colored2
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/colored2-3.1.2
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/colored2-3.1.2.gem
%{geminstdir}/specifications/colored2-3.1.2.gemspec

%files gem-jwt
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/jwt-2.2.3
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/jwt-2.2.3.gem
%{geminstdir}/specifications/jwt-2.2.3.gemspec


%changelog
* Sun Oct 24 2021 Trevor Vaughan <tvaughan@onyxpoint.com> - 3.12.1-2
- Changed:
  - Release tag bump to account for ISO-related fixes

* Tue Oct 12 2021 Chris Tessmer <chris.tessmer@onyxpoint.com> - 3.12.1-1
- Changed:
  - Updated r10k gem to 3.12.1
  - gems are installed into the RPMs buildroot/geminstdir with `--env-shebang`
- Added:
  - New `excludes:` key to gems in `build/sources.yaml`
  - RPMs include `dist` tags
- Removed:
  - gettext RPM does not include gem's `samples/` directory

* Thu Oct 07 2021 Chris Tessmer <chris.tessmer@onyxpoint.com> - 3.11.0-1
- Fixed `rake pkg:gem` and `rake pkg:rpm` to ignore local gem environment
- Add generated .spec file to git, so `pkg:single` can build it

* Wed Sep 01 2021 Jeanne Greulich <jeanne.greulich@onyxpoint.com> - 3.11.0-1
- Updated source versions to use r10k 3.11.0 and its corresponding gems
- Update Rakefile task pkg:rpm to add macro brp_mangle_shebangs so the shebangs
  in bash files would be /usr/bin/env ruby instead of pointing to the system ruby.
- Gem jwt, has a non standard gemspec file name.  Added a check for this so
  it would build the gem.

* Wed Dec 09 2020 Chris Tessmer <chris.tessmer@onyxpoint.com> - 3.7.0-0
- Changed:
  - Updated source versions to use r10k 3.7.0 and its corresponding
    gem dependencies
  - The `colored` gem has been deprecated in favor of `colored2`
- Fixed:
  - Fixed `rake gem_update` to (mostly) correctly update `build/sources.yaml`
  - Re-enabled the simp community repo in acceptance tests
- Added:
  - Project README.md
  - Enhancements to `rake gem_update`:
    - Resolves r10k gem dependencies from the r10k gem on rubygems.org
    - Updates version, url, repo, and license
    - When it can't safely update a url, it will print a warning (helpful because log4r is a
    - Adds new gem deps, removes old ones
  - Enhancements to `rake pkg:gem`:
    - Hack for git clone of untagged `log4r` release
  - Removed:
    - Old hacks for `colored` gem

* Mon Jun 24 2019 Liz Nemsick <lnemsick.simp@gmail.com> - 3.3.0-0
- Updated source versions to use r10k 3.3.0 and its corresponding
  gem dependencies

* Wed May 22 2019 Jeanne Greulich <jeanne.greulich@onyxpoint.com> - 3.1.1-1
- version of multipart-post updates in sources

* Mon Apr 01 2019 Jeanne Greulich <jeanne.greulich@onyxpoint.com> - 3.1.1-0
- Updated source versions to use r10k 3.1.1 and updated
  dependency gems where possible.  Latest puppet_forge
  gem relies on faraday ~> 0.9.0 so that gem
  cannot be updated until next release of puppet_forge gem.
- Remove puppet 4 support.
- Updated the version of simp-rake-helpers in Gemfile
  because earlier version has r10k dependency set to ~> 2.2.
- Updated release for all dependencies so they would all be reinstalled
  in the new simp-r10k directory.  Gem dependencies were being installed
  in r10k-<version> directory.  If r10k was
  updated it create a new r10k-<version> directory but if dependencies had
  not been updated they were not reinstalled in new directory. To fix this
  the version number was removed off the gem sub-directory. The release
  versions had to be updated this one time to force reinstall in the new
  versionless directory.
- Add fixtures file so FIPS tests will pass.
- updated Gemfile for simp-beaker-helpers to include new functions used in
  testing

* Wed Jan 16 2019 Liz Nemsick <lnemsick.simp@gmail.com> - 2.6.2-2
- Fixed bug in which the simp-vendored-r10k package did not require
  the 'git' package

* Tue Jul 17 2018 Liz Nemsick <lnemsick.simp@gmail.com> - 2.6.2-1
- Fixed bug in RPM variable used in simp-vendored-r10k description
- Fixed bug in which release for r01k gem in sources.yaml was not being
  used for the RPM release number of simp-vendored-r10k and
  simp-vendored-r10k-doc packages.

* Wed Apr 18 2018 Nick Miller <nick.miller@onyxpoint.com> - 2.6.2-0
- Update rpm to include r10k 2.6.2 and other components.
- Gems are now built from source and not contained in the repo.
  See build/sources.yaml.
- Added a basic docker test: rake test

* Fri Sep 01 2017 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.2.2
- First release of r10k wrapper
