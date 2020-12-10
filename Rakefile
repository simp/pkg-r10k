require 'fileutils'
require 'find'
require 'rake/clean'
require 'rubygems'
require 'simp/rake'
require 'simp/rake/beaker'
require 'erb'
require 'yaml'
require 'rest-client'

pkg = Simp::Rake::Pkg.new(File.dirname(__FILE__))
# Simp::RakePkg decides where the RPM spec file for a project is in
# its constructor.  However, for this project, the spec file will be
# generated.  So need to tell it where the spec file will be found.
pkg.spec_file = File.join(File.dirname(__FILE__), 'build', 'simp-vendored-r10k.spec')

@rakefile_dir=File.dirname(__FILE__)
deps = YAML.load_file('build/sources.yaml')

CLEAN.include 'dist'
CLEAN.include 'pkg'
CLEAN.include 'src'
CLEAN.include 'build/simp-vendored-r10k.spec'
Find.find( @rakefile_dir ) do |path|
  if File.directory? path
    CLEAN.include path if File.basename(path) == 'tmp'
  else
    Find.prune
  end
end

desc 'Check out each r10k gem repository (uses build/sources.yaml)'
task :checkout do
  deps['gems'].each do |gem,data|
    FileUtils.mkdir_p 'src/gems'
    puts "Checkout out gem #{gem} #{data['version']}"
    Dir.chdir('src/gems') do
      unless File.exist?(File.join(gem, "#{gem}.gemspec"))
        if data['repo']
          `git clone -q #{data['repo']} #{gem}`
        else
          `git clone -q #{data['url']} #{gem}`
        end
      end

      Dir.chdir(gem) do
        sh 'git fetch -q'
        checkout_attempts = [
          "git checkout -q #{data['version']} 2> /dev/null",
          "git checkout -q v#{data['version']} 2> /dev/null",
        ]

        # The log4r github repo doesn't have any tags, and its last release
        # (1.1.10) was in 2012.  However, the master branch has accumulated
        # many more commits over the years (and some of them may have been
        # breaking changes: https://github.com/colbygk/log4r/issues/26)
        if data['repo'] == 'https://github.com/colbygk/log4r' && data['version'] == '1.1.10'
          # This is the commit the released log4r 1.1.10 gem was built from
          checkout_attempts << 'git checkout -q 40e2c2edd657a21b34f09dec7de238f348b6f428 2> /dev/null'
        end

        sh checkout_attempts.join(' || ')
      end
    end
  end
end

def sanitize_github_repo_uri(str)
  return unless (str =~ %r{\Ahttps?://github.com/})
  res = str.dup
  res.sub!(%r{\Ahttp:},'https:')
  res.sub!(%r{(https://github.com/[^/]+/[^/]+)/.*}, '\1')
  res.sub!(%r{/\Z},'')
  res
end

desc <<~DESC
  Update gems in build/sources.yaml to latest available versions

  This task will
DESC
task :gem_update, [:r10k_version] do |_t, args|
  version = args.with_defaults(r10k_version: nil)
  new_deps = Marshal.load(Marshal.dump(deps))
  require 'tmpdir'
  require 'rubygems/remote_fetcher' # needed this with Ruby 2.5
  require 'rubygems/name_tuple'     # needed this w/2.4 & 2.5
  dep = Gem::Dependency.new 'r10k', version
  set = Gem::RequestSet.new dep
  requests = set.resolve

  removed_gems = deps['gems'].keys - (requests.map{|r| r.name })
  removed_gems.each do |g|
      warn ''
      warn '!'*80
      warn "WARNING: **REMOVING GEM** (no longer required): '#{g}'"
      warn '!'*80
      new_deps['gems'].delete(g)
  end

  new_gems = []
  updated_gems = []
  requests.each do |r|
    data = nil
    data = new_deps['gems'][r.name] ||= {}

    if data.empty?
      warn '', '='*80, "WARNING: **NEW GEM** dependency found: '#{r.name}'", '='*80
    end

    data['release'] = (r.version.to_s == data['version'].to_s) ? data['release'] + 1 : 0
    data['version'] = r.version.to_s

    Gem.sources.to_a.each do |gem_src|
      url = "#{gem_src}/api/v2/rubygems/#{r.name}/versions/#{r.version}.json"
      j = RestClient.get url, {content_type: :json, accept: :json}
      api_data = JSON.parse(j)
      if api_data['licenses'] && api_data['licenses'] != data['license'].to_s
        data['license'] = api_data['licenses'].join(' or ')
      end
      data['license'] ||= 'UNKNOWN'

      if api_data['source_code_uri']
        a_uri = sanitize_github_repo_uri(api_data['source_code_uri'])
        g_uri = sanitize_github_repo_uri(data['repo'])

        unless a_uri == g_uri
          warn ''
          warn "'#{r.name}' gem repo source_code_uri is different than 'repo' URL in 'build/sources.yaml'"
          warn "              File: #{data['repo']}"
          warn "              Gem:  #{api_data['source_code_uri']}"
          warn "         CHECK MANUALLY!  (Keeping the old version in case the gem version is nonsense)"
        else
          data['repo'] = a_uri
        end
      end

      if (data['repo'] && r.full_spec.homepage != data['url']) || (!data['url'])
        data['url'] = r.full_spec.homepage
      end

      if data['url'] && !data['repo']
        data['repo'] ||= sanitize_github_repo_uri(data['url'])
      end
    end
  end

  new_deps['version'] = new_deps['gems']['r10k']['version']
  File.write('build/sources.yaml', new_deps.to_yaml)
end

task :rpms_present do
  rpms=Dir.glob('dist/simp-vendored-r10k-*.noarch.rpm')
  if rpms.empty?
    Rake::Task['pkg:rpm'].invoke
  end
end

namespace :pkg do
  directory 'dist'

  desc 'build rubygem sub-packages'
  task :gem => ['dist', :checkout] do
    deps['gems'].each do |gem,data|
      puts "Building gem #{gem} #{data['version']}"
      Dir.chdir("src/gems/#{gem}") do |d|
        # multi_json requires a signing key, we don't have one
        sh "sed -i '/signing_key/d' #{gem}.gemspec" if gem == 'multi_json'
        `gem build --silent #{gem}.gemspec`
        FileUtils.mkdir_p 'dist'
        FileUtils.mv Dir.glob('*.gem'), File.join(@rakefile_dir, 'dist')
      end
    end
  end

  desc 'Generate the rpm spec file using build/sources.yaml'
  task :rpmspec do
    changelog = File.read('CHANGELOG')

    f = File.open('build/simp-vendored-r10k.spec', 'w')
    f << ERB.new(File.read('build/simp-vendored-r10k.spec.erb'), nil, '-').result(binding)
    f.close
  end

  Rake::Task['pkg:rpm'].clear
  desc 'Build the rpms for all gems in the build/sources.yaml file'
  task :rpm => [:rpmspec,:gem] do
    version  = deps['version']
    release  = deps['gems']['r10k']['release'].nil? ? 0 : deps['gems']['r10k']['release']
    builddir = File.join('dist','RPMBUILD')

    FileUtils.mkdir_p 'dist'
    FileUtils.mkdir_p ['BUILD','BUILDROOT','RPMS','SOURCES','SPECS','SRPMS'].map { |e| File.join(builddir,e) }
    FileUtils.cp Dir.glob('dist/*.gem'), File.join(builddir, 'SOURCES')

    Dir.chdir(File.join('dist','tmp')) do
      sh "[ -e simp-vendored-r10k-#{version} ] || ln -s ../.. simp-vendored-r10k-#{version}"
      tar_cmd  = []
      tar_cmd << 'tar --dereference'
      tar_cmd << "--exclude=simp-vendored-r10k-#{version}/dist"
      tar_cmd << "--exclude=simp-vendored-r10k-#{version}/vendor"
      tar_cmd << "--exclude=simp-vendored-r10k-#{version}/.vendor"
      tar_cmd << "--exclude=simp-vendored-r10k-#{version}/.bundle"
      tar_cmd << "--exclude=simp-vendored-r10k-#{version}/spec/fixtures/modules"
      tar_cmd << '-czf'
      tar_cmd << "../RPMBUILD/SOURCES/simp-vendored-r10k-#{version}-#{release}.tar.gz"
      tar_cmd << "simp-vendored-r10k-#{version}"
      sh tar_cmd.join(' ')
    end
    FileUtils.rm_rf File.join('dist','tmp')

    buildroot  = File.join(Dir.pwd,builddir)
    src_cmd  = []
    src_cmd << 'rpmbuild'
    src_cmd << "-D '_topdir #{buildroot}'"
    src_cmd << '-v -bs build/simp-vendored-r10k.spec'
    sh src_cmd.join(' ')

    rpm_cmd  = []
    rpm_cmd << 'rpmbuild'
    rpm_cmd << "-D '_topdir #{buildroot}'"
    rpm_cmd << '-v -ba build/simp-vendored-r10k.spec'
    sh rpm_cmd.join(' ')

    FileUtils.cp Dir.glob('dist/RPMBUILD/RPMS/noarch/*.rpm'), 'dist'
  end

  Rake::Task[:rpm].prerequisites.unshift(:rpmspec)
  Rake::Task[:check_rpm_changelog].enhance [:rpmspec]
  Rake::Task[:create_tag_changelog].enhance [:rpmspec]

  # CAUTION: pkg:compare_latest_tag doesn't work with release-only version
  # differences in this project...
  Rake::Task[:compare_latest_tag].enhance [:rpmspec]
end

task :default do
  system('rake -T')
end
# Acceptance Tests
Simp::Rake::Beaker.new(File.dirname(__FILE__))

# make sure pkg:rpm is a prerequisite for beaker:suites
Rake::Task['beaker:suites'].enhance ['pkg:rpm']

# vim: syntax=ruby
