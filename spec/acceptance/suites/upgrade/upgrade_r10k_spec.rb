
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
  on(host, 'yum makecache')
end

def install_deps(host, osver)
  host.install_package('curl')
  host.install_package('createrepo')
  if osver > '6'
    host.install_package('yum-utils')
  end
end

def simp_deps_repo(host)
  install_simp_repos(host, ['simp_deps'])
  on(host, 'yum makecache')
end

test_name 'upgrade simp vendored r10k'

describe 'upgrade simp vendored r10k' do

  hosts.each do |host|

    let(:dist_dir) { File.join(File.dirname(__FILE__), '../../../../dist/') }

    let(:expected_version) {  %x{rpm -qp "#{dist_dir}/simp-vendored-r10k-gem-r10k*.rpm" --info | grep Version}.split(':')[1].strip }

    osmajver = fact_on(host, 'operatingsystemmajrelease')

    context "install simp_vendored r10k from simp deps repo on el#{osmajver}" do

      it "should install repos" do
        if osmajver >= '8'
          skip("Can't run this test on EL8 until the EL8 simp erpos get setup")
        else
          install_deps(host, osmajver)
          simp_deps_repo(host)
          on(host, 'yum install -y simp-vendored-r10k')
          on(host, 'echo "run r10k first time";/usr/share/simp/bin/r10k version')
        end
      end

      it "should install and run the new version r10k" do
        if osmajver >= '8'
          skip("Can't run this test on EL8 until the EL8 simp erpos get setup")
        else
          create_repo(host, '/rpms', dist_dir)
          on(host, 'yum update -y --nogpgcheck')
          result = on(host, '/usr/share/simp/bin/r10k version').stdout
          expect(result.strip).to eq("r10k #{expected_version}")
        end
      end
    end
  end
end
