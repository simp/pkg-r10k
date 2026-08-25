require 'spec_helper_acceptance'

def create_repo(host, repo_dir, dist_dir)
  fail("Distribution Directory #{dist_dir} could not be found") unless Dir.exist?(dist_dir)

  on(host, "mkdir -p #{repo_dir}")
  scp_to(host, dist_dir, repo_dir)
  on(host, "cd #{repo_dir}; createrepo -p .")

  repo_file = <<~REPO
    [simp-vendored-r10k-local]
    name=Local simp-vendored-r10k test packages
    baseurl=file://#{repo_dir}
    enabled=1
    gpgcheck=0
  REPO
  create_remote_file(host, '/etc/yum.repos.d/simp-vendored-r10k-local.repo', repo_file)
end

def install_deps(host)
  host.install_package('createrepo_c')
end

test_name 'build simp vendored r10k'

describe 'build simp vendored r10k' do
  hosts.each do |host|
    let(:dist_dir) { File.join(File.dirname(__FILE__), '../../../../dist') }

    context "install simp-vendored-r10k on #{host}" do
      it 'should install repos' do
        install_deps(host)
        create_repo(host, '/rpms', dist_dir)
      end

      it 'should install and run r10k' do
        on(host, 'yum install -y --nogpgcheck simp-vendored-r10k')
        on(host, '/usr/share/simp/bin/r10k version')
      end

      it 'should deploy modules from a Puppetfile' do
        puppetfile = <<~PUPPETFILE
          mod 'simp_simplib',
            :git => 'https://github.com/simp/pupmod-simp-simplib',
            :branch => 'master'
        PUPPETFILE
        on(host, 'mkdir -p /root/r10k-test')
        create_remote_file(host, '/root/r10k-test/Puppetfile', puppetfile)
        on(host, 'cd /root/r10k-test; /usr/share/simp/bin/r10k puppetfile install')
        on(host, 'test -f /root/r10k-test/modules/simp_simplib/metadata.json')
      end
    end
  end
end
