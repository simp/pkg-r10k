require 'spec_helper'

describe R10K::Git::Rugged::Credentials, :unless => R10K::Util::Platform.jruby? do
  before(:all) do
    require 'r10k/git/rugged/credentials'
    require 'rugged/credentials'
  end

  let(:repo) { R10K::Git::Rugged::BareRepository.new("/some/nonexistent/path", "repo.git") }

  subject { described_class.new(repo) }

  after(:all) { R10K::Git.settings.reset! }

  describe "determining the username" do
    before { R10K::Git.settings[:username] = "moderns" }
    after { R10K::Git.settings.reset! }

    it "prefers a username from the URL" do
      user = subject.get_git_username("https://tessier-ashpool.freeside/repo.git", "ashpool")
      expect(user).to eq "ashpool"
    end

    it "uses the username from the Git config when specified" do
      user = subject.get_git_username("https://tessier-ashpool.freeside/repo.git", nil)
      expect(user).to eq "moderns"
    end

    it "falls back to the current user" do
      R10K::Git.settings.reset!
      expect(Etc).to receive(:getlogin).and_return("finn")
      user = subject.get_git_username("https://tessier-ashpool.freeside/repo.git", nil)
      expect(user).to eq "finn"
    end
  end

  describe "generating ssh key credentials" do
    after(:each) { R10K::Git.settings.reset! }

    it "prefers a per-repository SSH private key" do
      allow(File).to receive(:readable?).with("/etc/puppetlabs/r10k/ssh/tessier-ashpool-id_rsa").and_return true
      R10K::Git.settings[:repositories] = [{ remote: "ssh://git@tessier-ashpool.freeside/repo.git",
        private_key: "/etc/puppetlabs/r10k/ssh/tessier-ashpool-id_rsa"}]
      creds = subject.get_ssh_key_credentials("ssh://git@tessier-ashpool.freeside/repo.git", nil)
      expect(creds).to be_a_kind_of(Rugged::Credentials::SshKey)
      expect(creds.instance_variable_get(:@privatekey)).to eq("/etc/puppetlabs/r10k/ssh/tessier-ashpool-id_rsa")
    end

    it "falls back to the global SSH private key" do
      allow(File).to receive(:readable?).with("/etc/puppetlabs/r10k/ssh/id_rsa").and_return true
      R10K::Git.settings[:private_key] = "/etc/puppetlabs/r10k/ssh/id_rsa"
      creds = subject.get_ssh_key_credentials("ssh://git@tessier-ashpool.freeside/repo.git", nil)
      expect(creds).to be_a_kind_of(Rugged::Credentials::SshKey)
      expect(creds.instance_variable_get(:@privatekey)).to eq("/etc/puppetlabs/r10k/ssh/id_rsa")
    end

    it "raises an error if no key has been set" do
      R10K::Git.settings[:private_key] = nil
      expect {
        subject.get_ssh_key_credentials("https://tessier-ashpool.freeside/repo.git", nil)
      }.to raise_error(R10K::Git::GitError, /no private key was given/)
    end

    it "raises an error if the private key is unreadable" do
      R10K::Git.settings[:private_key] = "/some/nonexistent/.ssh/key"
      expect(File).to receive(:readable?).with("/some/nonexistent/.ssh/key").and_return false
      expect {
        subject.get_ssh_key_credentials("https://tessier-ashpool.freeside/repo.git", nil)
      }.to raise_error(R10K::Git::GitError, /Unable to use SSH key auth for.*is missing or unreadable/)
    end

    it "generates the rugged sshkey credential type" do
      allow(File).to receive(:readable?).with("/etc/puppetlabs/r10k/ssh/id_rsa").and_return true
      R10K::Git.settings[:private_key] = "/etc/puppetlabs/r10k/ssh/id_rsa"
      creds = subject.get_ssh_key_credentials("https://tessier-ashpool.freeside/repo.git", nil)
      expect(creds).to be_a_kind_of(Rugged::Credentials::SshKey)
      expect(creds.instance_variable_get(:@privatekey)).to eq("/etc/puppetlabs/r10k/ssh/id_rsa")
    end
  end

  describe "generating default credentials" do
    it "generates the rugged default credential type" do
      creds = subject.get_default_credentials("https://azurediamond:hunter2@tessier-ashpool.freeside/repo.git", "azurediamond")
      expect(creds).to be_a_kind_of(Rugged::Credentials::Default)
    end
  end

  describe "generating credentials" do
    it "creates ssh key credentials for the sshkey allowed type" do
      allow(File).to receive(:readable?).with("/etc/puppetlabs/r10k/ssh/id_rsa").and_return true
      R10K::Git.settings[:private_key] = "/etc/puppetlabs/r10k/ssh/id_rsa"
      expect(subject.call("https://tessier-ashpool.freeside/repo.git", nil, [:ssh_key])).to be_a_kind_of(Rugged::Credentials::SshKey)
    end

    it "creates user/password credentials for the default allowed type" do
      expect(subject.call("https://tessier-ashpool.freeside/repo.git", nil, [:plaintext])).to be_a_kind_of(Rugged::Credentials::UserPassword)
    end

    it "creates default credentials when no other types are allowed" do
      expect(subject.call("https://tessier-ashpool.freeside/repo.git", nil, [])).to be_a_kind_of(Rugged::Credentials::Default)
    end
  end
end
