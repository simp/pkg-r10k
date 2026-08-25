%global pkgname simp-r10k

%global gemdir /usr/share/simp/ruby
%global simp_bindir /usr/share/simp/bin
%global geminstdir %{gemdir}/%{pkgname}

%global r10k_version 5.0.3

# gem2ruby's method of installing gems into mocked build roots will blow up
# unless this line is present:
%define _unpackaged_files_terminate_build 0

Summary: r10k with puppet-safe gem installation
Name: simp-vendored-r10k
Version: %{r10k_version}
Release: 1%{?dist}
Group: Development/Languages
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
Source0: %{name}-%{version}-%{release}.tar.gz
Recommends: git
Recommends: (openvox-agent or puppet-agent)
Requires: %{name}-doc
Requires: rubygem(%{pkgname}-r10k) >= %{r10k_version}
Requires: rubygem(%{pkgname}-cri) >= 2.15.12
Requires: rubygem(%{pkgname}-faraday) >= 2.14.3
Requires: rubygem(%{pkgname}-fast_gettext) >= 4.1.1
Requires: rubygem(%{pkgname}-gettext) >= 3.5.2
Requires: rubygem(%{pkgname}-gettext-setup) >= 1.1.1
Requires: rubygem(%{pkgname}-locale) >= 2.1.5
Requires: rubygem(%{pkgname}-log4r) >= 1.1.10
Requires: rubygem(%{pkgname}-minitar) >= 1.1.0
Requires: rubygem(%{pkgname}-multi_json) >= 1.21.1
Requires: rubygem(%{pkgname}-puppet_forge) >= 6.2.0
Requires: rubygem(%{pkgname}-r10k) >= 5.0.3
Requires: rubygem(%{pkgname}-semantic_puppet) >= 1.1.1
Requires: rubygem(%{pkgname}-text) >= 1.3.1
Requires: rubygem(%{pkgname}-colored2) >= 4.0.3
Requires: rubygem(%{pkgname}-jwt) >= 2.10.3
Requires: rubygem(%{pkgname}-faraday-net_http) >= 3.4.4
Requires: rubygem(%{pkgname}-faraday-follow_redirects) >= 0.5.0
Requires: rubygem(%{pkgname}-erubi) >= 1.13.1
Requires: rubygem(%{pkgname}-logger) >= 1.7.0
Requires: rubygem(%{pkgname}-uri) >= 1.1.1
Requires: rubygem(%{pkgname}-net-http) >= 0.9.1
Requires: rubygem(%{pkgname}-base64) >= 0.3.0
Requires: rubygem(%{pkgname}-singleton) >= 0.3.0
Requires: rubygem(%{pkgname}-forwardable) >= 1.4.0
Requires: rubygem(%{pkgname}-prime) >= 0.1.4
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
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/simp/pkg-r10k
BuildArch: noarch

%description doc

Documentation for the SIMP r10k installation including sample configuration and
postrun scripts suited to a SIMP environment.

%package gem-cri
Summary: A cri Gem for use with %{name}
Version: 2.15.12
Release: 1%{?dist}
License: MIT
URL: https://github.com/ddfreyne/cri
Source11: cri-2.15.12.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-cri) = 2.15.12

%description gem-cri

Gem dependency for %{name}

%package gem-faraday
Summary: A faraday Gem for use with %{name}
Version: 2.14.3
Release: 1%{?dist}
License: MIT
URL: https://lostisland.github.io/faraday
Source12: faraday-2.14.3.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday) = 2.14.3
Obsoletes: simp-vendored-r10k-gem-faraday_middleware < 0.15.0
Obsoletes: simp-vendored-r10k-gem-multipart-post < 2.2.0

%description gem-faraday

Gem dependency for %{name}

%package gem-fast_gettext
Summary: A fast_gettext Gem for use with %{name}
Version: 4.1.1
Release: 1%{?dist}
License: MIT or Ruby
URL: https://github.com/grosser/fast_gettext
Source13: fast_gettext-4.1.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-fast_gettext) = 4.1.1

%description gem-fast_gettext

Gem dependency for %{name}

%package gem-gettext
Summary: A gettext Gem for use with %{name}
Version: 3.5.2
Release: 1%{?dist}
License: Ruby or LGPL-3.0+
URL: https://ruby-gettext.github.io/
Source14: gettext-3.5.2.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-gettext) = 3.5.2

%description gem-gettext

Gem dependency for %{name}

%package gem-gettext-setup
Summary: A gettext-setup Gem for use with %{name}
Version: 1.1.1
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/gettext-setup-gem
Source15: gettext-setup-1.1.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-gettext-setup) = 1.1.1

%description gem-gettext-setup

Gem dependency for %{name}

%package gem-locale
Summary: A locale Gem for use with %{name}
Version: 2.1.5
Release: 1%{?dist}
License: Ruby or LGPL-3.0-or-later
URL: https://github.com/ruby-gettext/locale
Source16: locale-2.1.5.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-locale) = 2.1.5

%description gem-locale

Gem dependency for %{name}

%package gem-log4r
Summary: A log4r Gem for use with %{name}
Version: 1.1.10
Release: 5%{?dist}
License: MIT
URL: http://log4r.rubyforge.org
Source17: log4r-1.1.10.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-log4r) = 1.1.10

%description gem-log4r

Gem dependency for %{name}

%package gem-minitar
Summary: A minitar Gem for use with %{name}
Version: 1.1.0
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/halostatue/minitar
Source18: minitar-1.1.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-minitar) = 1.1.0

%description gem-minitar

Gem dependency for %{name}

%package gem-multi_json
Summary: A multi_json Gem for use with %{name}
Version: 1.21.1
Release: 1%{?dist}
License: MIT
URL: https://github.com/sferik/multi_json
Source19: multi_json-1.21.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-multi_json) = 1.21.1

%description gem-multi_json

Gem dependency for %{name}

%package gem-puppet_forge
Summary: A puppet_forge Gem for use with %{name}
Version: 6.2.0
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/forge-ruby
Source20: puppet_forge-6.2.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-puppet_forge) = 6.2.0

%description gem-puppet_forge

Gem dependency for %{name}

%package gem-r10k
Summary: A r10k Gem for use with %{name}
Version: 5.0.3
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/r10k
Source21: r10k-5.0.3.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-r10k) = 5.0.3

%description gem-r10k

Gem dependency for %{name}

%package gem-semantic_puppet
Summary: A semantic_puppet Gem for use with %{name}
Version: 1.1.1
Release: 1%{?dist}
License: Apache-2.0
URL: https://github.com/puppetlabs/semantic_puppet
Source22: semantic_puppet-1.1.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-semantic_puppet) = 1.1.1

%description gem-semantic_puppet

Gem dependency for %{name}

%package gem-text
Summary: A text Gem for use with %{name}
Version: 1.3.1
Release: 4%{?dist}
License: MIT
URL: http://github.com/threedaymonk/text
Source23: text-1.3.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-text) = 1.3.1

%description gem-text

Gem dependency for %{name}

%package gem-colored2
Summary: A colored2 Gem for use with %{name}
Version: 4.0.3
Release: 1%{?dist}
License: MIT
URL: http://github.com/kigster/colored2
Source24: colored2-4.0.3.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-colored2) = 4.0.3
Obsoletes: simp-vendored-r10k-gem-colored < 2.0

%description gem-colored2

Gem dependency for %{name}

%package gem-jwt
Summary: A jwt Gem for use with %{name}
Version: 2.10.3
Release: 1%{?dist}
License: MIT
URL: https://github.com/jwt/ruby-jwt
Source25: jwt-2.10.3.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-jwt) = 2.10.3

%description gem-jwt

Gem dependency for %{name}

%package gem-faraday-net_http
Summary: A faraday-net_http Gem for use with %{name}
Version: 3.4.4
Release: 1%{?dist}
License: MIT
URL: https://github.com/lostisland/faraday-net_http
Source26: faraday-net_http-3.4.4.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday-net_http) = 3.4.4

%description gem-faraday-net_http

Gem dependency for %{name}

%package gem-faraday-follow_redirects
Summary: A faraday-follow_redirects Gem for use with %{name}
Version: 0.5.0
Release: 1%{?dist}
License: MIT
URL: https://github.com/tisba/faraday-follow-redirects
Source27: faraday-follow_redirects-0.5.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-faraday-follow_redirects) = 0.5.0

%description gem-faraday-follow_redirects

Gem dependency for %{name}

%package gem-erubi
Summary: A erubi Gem for use with %{name}
Version: 1.13.1
Release: 1%{?dist}
License: MIT
URL: https://github.com/jeremyevans/erubi
Source28: erubi-1.13.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-erubi) = 1.13.1

%description gem-erubi

Gem dependency for %{name}

%package gem-logger
Summary: A logger Gem for use with %{name}
Version: 1.7.0
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/logger
Source29: logger-1.7.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-logger) = 1.7.0

%description gem-logger

Gem dependency for %{name}

%package gem-uri
Summary: A uri Gem for use with %{name}
Version: 1.1.1
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/uri
Source30: uri-1.1.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-uri) = 1.1.1

%description gem-uri

Gem dependency for %{name}

%package gem-net-http
Summary: A net-http Gem for use with %{name}
Version: 0.9.1
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/net-http
Source31: net-http-0.9.1.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-net-http) = 0.9.1

%description gem-net-http

Gem dependency for %{name}

%package gem-base64
Summary: A base64 Gem for use with %{name}
Version: 0.3.0
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/base64
Source32: base64-0.3.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-base64) = 0.3.0

%description gem-base64

Gem dependency for %{name}

%package gem-singleton
Summary: A singleton Gem for use with %{name}
Version: 0.3.0
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/singleton
Source33: singleton-0.3.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-singleton) = 0.3.0

%description gem-singleton

Gem dependency for %{name}

%package gem-forwardable
Summary: A forwardable Gem for use with %{name}
Version: 1.4.0
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/forwardable
Source34: forwardable-1.4.0.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-forwardable) = 1.4.0

%description gem-forwardable

Gem dependency for %{name}

%package gem-prime
Summary: A prime Gem for use with %{name}
Version: 0.1.4
Release: 1%{?dist}
License: Ruby or BSD-2-Clause
URL: https://github.com/ruby/prime
Source35: prime-0.1.4.gem
BuildArch: noarch
Provides: rubygem(%{pkgname}-prime) = 0.1.4

%description gem-prime

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
  for i=11,35 do
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
%{geminstdir}/gems/cri-2.15.12
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/cri-2.15.12.gem
%{geminstdir}/specifications/cri-2.15.12.gemspec

%files gem-faraday
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday-2.14.3
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/faraday-2.14.3.gem
%{geminstdir}/specifications/faraday-2.14.3.gemspec

%files gem-fast_gettext
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/fast_gettext-4.1.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/fast_gettext-4.1.1.gem
%{geminstdir}/specifications/fast_gettext-4.1.1.gemspec

%files gem-gettext
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/gettext-3.5.2
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/gettext-3.5.2.gem
%exclude %{geminstdir}/gems/gettext-3.5.2/samples
%{geminstdir}/specifications/gettext-3.5.2.gemspec

%files gem-gettext-setup
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/gettext-setup-1.1.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/gettext-setup-1.1.1.gem
%{geminstdir}/specifications/gettext-setup-1.1.1.gemspec

%files gem-locale
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/locale-2.1.5
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/locale-2.1.5.gem
%{geminstdir}/specifications/locale-2.1.5.gemspec

%files gem-log4r
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/log4r-1.1.10
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/log4r-1.1.10.gem
%{geminstdir}/specifications/log4r-1.1.10.gemspec

%files gem-minitar
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/minitar-1.1.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/minitar-1.1.0.gem
%{geminstdir}/specifications/minitar-1.1.0.gemspec

%files gem-multi_json
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/multi_json-1.21.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/multi_json-1.21.1.gem
%{geminstdir}/specifications/multi_json-1.21.1.gemspec

%files gem-puppet_forge
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/puppet_forge-6.2.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/puppet_forge-6.2.0.gem
%{geminstdir}/specifications/puppet_forge-6.2.0.gemspec

%files gem-r10k
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/r10k-5.0.3
%attr(0755,-,-) %{geminstdir}/gems/r10k-5.0.3/bin/r10k
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/r10k-5.0.3.gem
%{geminstdir}/specifications/r10k-5.0.3.gemspec

%files gem-semantic_puppet
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/semantic_puppet-1.1.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/semantic_puppet-1.1.1.gem
%{geminstdir}/specifications/semantic_puppet-1.1.1.gemspec

%files gem-text
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/text-1.3.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/text-1.3.1.gem
%{geminstdir}/specifications/text-1.3.1.gemspec

%files gem-colored2
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/colored2-4.0.3
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/colored2-4.0.3.gem
%{geminstdir}/specifications/colored2-4.0.3.gemspec

%files gem-jwt
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/jwt-2.10.3
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/jwt-2.10.3.gem
%{geminstdir}/specifications/jwt-2.10.3.gemspec

%files gem-faraday-net_http
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday-net_http-3.4.4
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/faraday-net_http-3.4.4.gem
%{geminstdir}/specifications/faraday-net_http-3.4.4.gemspec

%files gem-faraday-follow_redirects
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/faraday-follow_redirects-0.5.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/faraday-follow_redirects-0.5.0.gem
%{geminstdir}/specifications/faraday-follow_redirects-0.5.0.gemspec

%files gem-erubi
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/erubi-1.13.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/erubi-1.13.1.gem
%{geminstdir}/specifications/erubi-1.13.1.gemspec

%files gem-logger
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/logger-1.7.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/logger-1.7.0.gem
%{geminstdir}/specifications/logger-1.7.0.gemspec

%files gem-uri
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/uri-1.1.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/uri-1.1.1.gem
%{geminstdir}/specifications/uri-1.1.1.gemspec

%files gem-net-http
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/net-http-0.9.1
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/net-http-0.9.1.gem
%{geminstdir}/specifications/net-http-0.9.1.gemspec

%files gem-base64
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/base64-0.3.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/base64-0.3.0.gem
%{geminstdir}/specifications/base64-0.3.0.gemspec

%files gem-singleton
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/singleton-0.3.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/singleton-0.3.0.gem
%{geminstdir}/specifications/singleton-0.3.0.gemspec

%files gem-forwardable
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/forwardable-1.4.0
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/forwardable-1.4.0.gem
%{geminstdir}/specifications/forwardable-1.4.0.gemspec

%files gem-prime
%defattr(0644, root, root, 0755)
%{geminstdir}/gems/prime-0.1.4
%exclude %{geminstdir}/bin
%exclude %{geminstdir}/cache/prime-0.1.4.gem
%{geminstdir}/specifications/prime-0.1.4.gemspec


%changelog
* Tue Aug 25 2026 Steven Pritchard <steve@sicura.us> - 5.0.3-1
- Changed:
  - Updated `r10k` gem to 5.0.3
  - See https://github.com/puppetlabs/r10k/compare/3.14.2...5.0.3
    for full diff of r10k changes
  - Updated all vendored dependency gems to current versions
  - RPM now `Recommends: (openvox-agent or puppet-agent)` instead of
    `puppet-agent`, following the SIMP migration to OpenVox
  - Build tooling now requires Ruby 3.2+ (tested through Ruby 4.0),
    the `openvox` gem, and `simp-rake-helpers` 6.x
- Added:
  - New vendored gems required by r10k 5:
    `erubi`, `faraday-follow_redirects`, `faraday-net_http`
  - New `exclude_gems` key in `build/sources.yaml` lists dependencies
    that ship with the AIO agent's Ruby and are no longer vendored
    (base64, fiddle, forwardable, json, logger, net-http, prime, racc,
    singleton, uri)
- Removed:
  - Dropped vendored gems no longer required by r10k:
    `faraday_middleware`, `multipart-post`
  - Dropped support for EL7 (packages are built for EL8, EL9, and EL10)

* Mon Apr 25 2022 Chris Tessmer <chris.tessmer@onyxpoint.com> - 3.14.2-1
- Changed:
  - Updated `r10k` gem to 3.14.2
  - Updated dependency `faraday` gem to 0.17.5
  - See https://github.com/puppetlabs/r10k/compare/3.12.1...3.14.2
    for full diff of r10k changes
- Added:
  - New r10k gem features:
    - New config: `oauth token` for rugged provider
    - Config: `exclude_spec` in `r10k.yaml`, `Puppetfile`, and CLI
    - Add support for `plain` environment type, to allow sources that support
      environment modules to operate without a control repo being required.
    - Add support for `tarball` module type, allowing module content to be
      packaged and sourced from generic fileservers
    - Add experimental support for tarball environment type, allowing whole
      environments to be packaged and sourced from generic fileservers
    - Add support for specifying additional logging ouputs
- Fixed:
  - Fixes to the r10k gem:
    - Record unprocessed environment name, so that `strip_component` does not
      cause truncated environment names to be used as git branches, resulting
      in errors or incorrect deploys.
    - Ensure `--incremental` does not skip undeployed modules
    - Fix `force` always resolving to true for `puppetfile install`
    - Resync repos with unresolvable refs
    - Do not recurse into symlinked dirs when finding files to purge.
    - Restore Ruby 3 compatibility
    - Ensure the remote url in rugged cache directories is current



* Wed Feb 09 2022 Chris Tessmer <chris.tessmer@onyxpoint.com> - 3.12.1-4
- Fixed:
  - SRPMs are now copied into `dist/` during builds

* Mon Oct 25 2021 Chris Tessmer <chris.tessmer@onyxpoint.com> - 3.12.1-3
- Changed:
  - RPM for `colored2` gem now obsoletes RPMs for older `colored` gem
- Added:
  - New `sources.yaml` keys for arbitrary `obsoletes`, `requires`,
    `conflicts`, and `provides`

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
