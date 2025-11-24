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
# renovate: datasource=rubygems versioning=ruby
gem 'puppet', ENV.fetch('PUPPET_VERSION',  '~> 7')
gem 'rake'
  # renovate: datasource=rubygems versioning=ruby
  gem 'simp-rake-helpers', ENV.fetch('SIMP_RAKE_HELPERS_VERSION', '~> 5.24.0')

# renovate: datasource=rubygems versioning=ruby
gem 'r10k', ENV.fetch('R10K_VERSION', '5.0.2')
gem 'rest-client'

group :testing do
  # bootstrap common environment variables
  gem 'dotenv'

  # Testing framework
  gem 'rspec'
  gem 'rspec-its'

  # A dependency of simp-rake-helpers
  # renovate: datasource=rubygems versioning=ruby
  gem 'simp-beaker-helpers', ENV.fetch('SIMP_BEAKER_HELPERS_VERSION', '~> 2.0.0')

end

# Evaluate extra gemfiles if they exist
extra_gemfiles = [
  ENV['EXTRA_GEMFILE'] || '',
  "#{__FILE__}.project",
  "#{__FILE__}.local",
  File.join(Dir.home, '.gemfile'),
]
extra_gemfiles.each do |gemfile|
  if File.file?(gemfile) && File.readable?(gemfile)
    eval(File.read(gemfile), binding)
  end
end
