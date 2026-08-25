## pkg-r10k: simp-vendored R10K gem-to-RPMs packager

#### Table of Contents

<!-- vim-markdown-toc GFM -->

* [Description](#description)
* [Setup](#setup)
  * [Requirements](#requirements)
  * [Getting started](#getting-started)
* [Usage](#usage)

<!-- vim-markdown-toc -->

## Description

This project builds a SIMP-vendored RPM of [r10k], which is intended to ensure that a known
version of r10k is present on the system.

* The build process creates RPMs for the r10k gem and each of its dependencies.
* The `r10k` executable is installed into `/usr/share/simp/bin/r10k`
* The installed `r10k` runs under the AIO agent's Ruby (OpenVox 8+ or
  puppet-agent), when available
* RPMs are built for EL (RHEL, AlmaLinux, Rocky Linux, Oracle Linux) 8, 9,
  and 10
* Gems that cannot be vendored noarch (C extensions) are listed under
  `exclude_gems` in `build/sources.yaml` and must be satisfied by the
  default/bundled gems shipped with the AIO agent's Ruby

## Setup

### Requirements

* [Ruby] 3.2 or later (tested with 3.2 through 4.0)
* [bundler]

### Getting started

```sh
git clone https://github.com/simp/pkg-r10k
cd pkg-r10k
bundle install
bundle exec rake -T
```

## Usage

To update to the latest version of r10k and package all its gems:

1. Update `build/sources.yaml` to the latest version of r10k

   ```sh
   bundle exec rake gem_update
   ```

   To review the changes:

   ```sh
   git diff build/sources.yaml
   ```

   To update to a specific version of r10k, run:
   ```sh
   bundle exec rake gem_update[<r10k_version>]
   ```

  If you have changed the packaging and need to update the release
  version for packages already released run

   ```sh
   R10K_force_release_update=yes bundle exec rake gem_update
   ```

2. Verify that the data in `build/sources.yaml` is correct

3. Check out gems and build RPMs using the data in `build/sources.yaml`

   ```sh
   bundle exec rake pkg:rpm
   ```

   The RPMs will be built under the `dist/` directory.

[r10k]: https://github.com/puppetlabs/r10k
[ruby]: https://www.ruby-lang.org/
[bundler]: https://bundler.io
