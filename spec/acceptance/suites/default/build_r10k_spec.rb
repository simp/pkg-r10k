
require 'spec_helper_acceptance'

def create_repo(host, repo_dir, dist_dir)
  if Dir.exists?(dist_dir)
    on(host, "mkdir -p #{repo_dir}")
    scp_to(host, dist_dir, repo_dir)
  else
    fail("Distribution Directory #{dist_dir} could not be found")
  end
  on(host, "cd #{repo_dir}; createrepo -p .")
  on(host, "yum-config-manager --add-repo file://#{repo_dir}")
end

def install_deps(host, osver)
  host.install_package('curl')
  host.install_package('createrepo')
  if osver > '6'
    host.install_package('yum-utils')
  end
end

test_name 'build simp vendored r10k'

describe 'build simp vendored r10k' do

  hosts.each do |host|
    let(:dist_dir) { File.join(File.dirname(__FILE__), '../../../../dist') }

    osmajver = fact_on(host, 'operatingsystemmajrelease')

    context 'install simp_vendored r10k' do
      it 'should install repos ' do
        install_deps(host, osmajver)
        create_repo(host, '/rpms', dist_dir)
      end

      it 'should install and run r10k' do
        on(host, 'yum install -y --nogpgcheck simp-vendored-r10k')
        on(host, '/usr/share/simp/bin/r10k')
      end

    end

  end
end
