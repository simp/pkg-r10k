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
* Tested against Puppet 5.5 and Puppet 6

## Setup

### Requirements

* [Ruby] (last tested with 2.4.9 and 2.5.7)
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

   To checkout a specifice version run:
   ```sh
   bundle exec rake gem_update[<version>]
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
