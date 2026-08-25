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
  on(host, 'yum makecache')
end

def install_deps(host)
  host.install_package('createrepo_c')
end

test_name 'upgrade simp vendored r10k'

describe 'upgrade simp vendored r10k' do
  hosts.each do |host|
    let(:dist_dir) { File.join(File.dirname(__FILE__), '../../../../dist/') }

    let(:expected_version) { %x{rpm -q --qf '%{version}\n' -p "#{dist_dir}/simp-vendored-r10k-gem-r10k"*.rpm}.strip }

    context "install simp-vendored-r10k from the SIMP community repo on #{host}" do
      it 'should install the previous release' do
        install_deps(host)
        install_simp_repos(host)
        on(host, 'yum makecache')

        result = on(host, 'yum install -y simp-vendored-r10k', accept_all_exit_codes: true)
        if result.exit_code != 0
          skip('simp-vendored-r10k is not yet available from the SIMP community repos for this OS')
        end
        on(host, 'echo "run r10k first time"; /usr/share/simp/bin/r10k version')
      end

      it 'should upgrade to and run the new version of r10k' do
        if on(host, 'rpm -q simp-vendored-r10k', accept_all_exit_codes: true).exit_code != 0
          skip('previous release could not be installed on this OS')
        end
        create_repo(host, '/rpms', dist_dir)
        on(host, 'yum update -y --nogpgcheck')
        result = on(host, '/usr/share/simp/bin/r10k version').stdout
        expect(result.strip).to eq("r10k #{expected_version}")
      end
    end
  end
end
