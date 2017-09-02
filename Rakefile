$: << File.expand_path( '../lib/', __FILE__ )

require 'fileutils'
require 'find'
require 'rake/clean'
require 'rspec/core/rake_task'
require 'rubygems'
require 'simp/rake'

Simp::Rake::Pkg.new(File.dirname(__FILE__))

@package='simp-cli'
@rakefile_dir=File.dirname(__FILE__)


CLEAN.include "#{@package}-*.gem"
CLEAN.include 'coverage'
CLEAN.include 'dist'
CLEAN.include 'pkg'
Find.find( @rakefile_dir ) do |path|
  if File.directory? path
    CLEAN.include path if File.basename(path) == 'tmp'
  else
    Find.prune
  end
end


desc 'special notes about these rake commands'
task :help do
  puts %Q{
== Environment Variables ==
SIMP_RPM_BUILD     when set, alters the gem produced by pkg:gem to be RPM-safe.
                   'pkg:gem' sets this automatically.
== Restrictions ==
- Because the code for this gem uses a global, singleton HighLine object,
  the tests for this code cannot be parallelized.
- To prevent actual changes from being made to your system, some of the
  'simp config' tests fail if the tests are run as root.
  }
end

desc "Run spec tests"
RSpec::Core::RakeTask.new(:spec) do |t|
  t.rspec_opts = ['--color']
  t.pattern = 'spec/**/*_spec.rb'
end

namespace :pkg do
  @specfile_template = "rubygem-#{@package}.spec.template"
  @specfile          = "build/rubygem-#{@package}.spec"

  # ----------------------------------------
  # DO NOT UNCOMMENT THIS: the spec file requires a lot of tweaking
  # ----------------------------------------
  #  desc "generate RPM spec file for #{@package}"
  #  task :spec => [:clean, :gem] do
  #    Dir.glob("pkg/#{@package}*.gem") do |pkg|
  #      sh %Q{gem2rpm -t "#{@specfile_template}" "#{pkg}" > "#{@specfile}"}
  #    end
  #  end

  directory 'dist'

  desc "build rubygem sub-packages for #{@package}"
  task :gem => ['dist'] do
    gem_dirs = Dir.glob('ext/gems/*')

    gem_dirs.each do |gem_dir|
      Dir.chdir gem_dir do
        Dir['*.gemspec'].each do |spec_file|
          cmd = %Q{SIMP_RPM_BUILD=1 bundle exec gem build "#{spec_file}" &> /dev/null}
          sh cmd
          FileUtils.mkdir_p 'dist'
          FileUtils.mv Dir.glob('*.gem'), File.join(@rakefile_dir, 'dist')
        end
      end
    end
  end

  Rake::Task[:rpm].prerequisites.unshift(:gem)
end
# vim: syntax=ruby
