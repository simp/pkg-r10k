# Gemfile for bundler (gem install bundler)
#
# To update all gem dependencies:
#
#   bundle
#
# To run a rake task:
#
#   bundle exec rake <task>
# Variables:
#
# SIMP_GEM_SERVERS | a space/comma delimited list of rubygem servers
# PUPPET_VERSION   | specifies the version of the puppet gem to load
# ------------------------------------------------------------------------------
gem_sources   = ENV.key?('SIMP_GEM_SERVERS') ? ENV['SIMP_GEM_SERVERS'].split(/[, ]+/) : ['https://rubygems.org']

gem_sources.each { |gem_source| source gem_source }

# mandatory gems
gem 'mg'
gem 'puppet', ENV.fetch('PUPPET_VERSION',  '~> 6.2')
gem 'rake'
gem 'simp-rake-helpers', ENV.fetch('SIMP_RAKE_HELPERS_VERSION', ['>= 5.12.1', '< 6'])

gem 'r10k', ENV.fetch('R10K_VERSION', '3.11')
gem 'rest-client'

group :testing do
  # bootstrap common environment variables
  gem 'dotenv'

  # Testing framework
  gem 'rspec'
  gem 'rspec-its'

  # A dependency of simp-rake-helpers
  gem 'simp-beaker-helpers', ENV['SIMP_BEAKER_HELPERS_VERSION'] || ['>= 1.23.2', '< 2']

end
