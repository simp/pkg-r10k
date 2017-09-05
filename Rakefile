$: << File.expand_path( '../lib/', __FILE__ )

require 'fileutils'
require 'find'
require 'rake/clean'
require 'rubygems'
require 'simp/rake'

Simp::Rake::Pkg.new(File.dirname(__FILE__))

@rakefile_dir=File.dirname(__FILE__)

CLEAN.include 'dist'
CLEAN.include 'pkg'
Find.find( @rakefile_dir ) do |path|
  if File.directory? path
    CLEAN.include path if File.basename(path) == 'tmp'
  else
    Find.prune
  end
end

namespace :pkg do
  directory 'dist'

  desc 'build rubygem sub-packages'
  task :gem => ['dist'] do
    gem_dirs = Dir.glob('ext/gems/*')

    gem_dirs.each do |gem_dir|
      Dir.chdir gem_dir do
        Dir['*.gemspec'].each do |spec_file|
          cmd = %Q{bundle exec gem build "#{spec_file}" &> /dev/null}
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
