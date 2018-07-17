require 'fileutils'
require 'find'
require 'rake/clean'
require 'rubygems'
require 'simp/rake'
require 'erb'
require 'yaml'

Simp::Rake::Pkg.new(File.dirname(__FILE__))

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

task :checkout do
  deps['gems'].each do |gem,data|
    FileUtils.mkdir_p 'src/gems'
      Dir.chdir('src/gems') do
      next if Dir.exists? gem
      if data['repo']
        `git clone -q #{data['repo']} #{gem}`
      else
        `git clone -q #{data['url']} #{gem}`
      end
      Dir.chdir(gem) do
        `git fetch -q`
        `git checkout -q #{data['version']} 2> /dev/null`
        `git checkout -q v#{data['version']} 2> /dev/null`
      end
    end
  end
end

task :gem_update do
  deps['gems'].each do |gem,data|
    data['version'] = Gem.latest_spec_for(gem).version.to_s
  end
  File.write('build/sources.yaml', deps.to_yaml)
end

task :test, [:el_version] do |t, args|
  el = args[:el_version] || '7'

  docker_cmd  = []
  docker_cmd << 'docker run -it'
  docker_cmd << '-v `pwd`/dist:/rpms:Z'
  docker_cmd << '-w /rpms'
  docker_cmd << "centos:#{el}"
  docker_cmd << '/bin/bash -c "'
  docker_cmd <<   "yum install -y http://yum.puppetlabs.com/puppetlabs-release-pc1-el-#{el}.noarch.rpm &&"
  docker_cmd <<   'yum install -y yum-utils &&' if el.to_i == 6
  docker_cmd <<   'yum install -y createrepo &&'
  docker_cmd <<   'createrepo -p . &&'
  docker_cmd <<   'yum-config-manager --add-repo file:///rpms &&'
  docker_cmd <<   'yum install -y --nogpgcheck simp-vendored-r10k &&'
  docker_cmd <<   'rm -rf /rpms/repodata &&'
  docker_cmd <<   '/usr/share/simp/bin/r10k'
  docker_cmd << '"'
  sh docker_cmd.join(' ')
end

task :test_upgrade, [:el_version] do |t, args|
  el = args[:el_version] || '7'

  docker_cmd  = []
  docker_cmd << 'docker run -it'
  docker_cmd << '-v `pwd`/dist:/rpms:Z'
  docker_cmd << '-w /rpms'
  docker_cmd << "centos:#{el}"
  docker_cmd << '/bin/bash -c "'
  docker_cmd <<   'yum install -y yum-utils &&' if el.to_i == 6
  docker_cmd <<   "yum install -y http://yum.puppetlabs.com/puppetlabs-release-pc1-el-#{el}.noarch.rpm &&"
  docker_cmd <<   'yum install -y createrepo &&'
  docker_cmd <<   "yum-config-manager --add-repo https://packagecloud.io/simp-project/6_X/el/#{el}/x86_64 &&"
  docker_cmd <<   'yum install -y --nogpgcheck simp-vendored-r10k &&'
  docker_cmd <<   '/usr/share/simp/bin/r10k &&'

  docker_cmd <<   'createrepo -p . &&'
  docker_cmd <<   'yum-config-manager --add-repo file:///rpms &&'
  docker_cmd <<   'yum update -y --nogpgcheck &&'
  docker_cmd <<   'rm -rf /rpms/repodata &&'
  docker_cmd <<   '/usr/share/simp/bin/r10k'
  docker_cmd << '"'
  sh docker_cmd.join(' ')
end

namespace :pkg do
  directory 'dist'

  desc 'build rubygem sub-packages'
  task :gem => ['dist', :checkout] do
    deps['gems'].each do |gem,data|
      Dir.chdir("src/gems/#{gem}") do |d|
        # multi_json requires a signing key, we don't have one
        sh "sed -i '/signing_key/d' #{gem}.gemspec" if gem == 'multi_json'
        # this is a very old gem and newer versions of rubygems require a LICENSE
        # the master branch has one but there will be no new release
        sh 'curl -s https://raw.githubusercontent.com/defunkt/colored/master/LICENSE > LICENSE' if gem == 'colored'

        `gem build --silent #{gem}.gemspec`
        FileUtils.mkdir_p 'dist'
        FileUtils.mv Dir.glob('*.gem'), File.join(@rakefile_dir, 'dist')
      end
    end
  end

  desc 'Generate the rpm spec file using build/sources.yaml'
  task :rpmspec => :gem do
    changelog = File.read('CHANGELOG')

    f = File.open('build/simp-vendored-r10k.spec', 'w')
    f << ERB.new(File.read('build/simp-vendored-r10k.spec.erb'), nil, '-').result(binding)
    f.close
  end

  Rake::Task['pkg:rpm'].clear
  desc 'Build the rpms for all gems in the build/sources.yaml file'
  task :rpm => :rpmspec do
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
      tar_cmd << "--exclude=simp-vendored-r10k-#{version}/.bundle"
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
end

task :default do
  system('rake -T')
end
# vim: syntax=ruby
