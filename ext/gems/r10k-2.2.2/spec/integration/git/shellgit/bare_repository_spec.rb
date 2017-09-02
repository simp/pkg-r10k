require 'spec_helper'
require 'r10k/git/shellgit/bare_repository'

describe R10K::Git::ShellGit::BareRepository do
  include_context 'Git integration'

  let(:dirname) { 'bare-repo.git' }

  subject { described_class.new(basedir, dirname) }

  it_behaves_like 'a git repository'
  it_behaves_like 'a git bare repository'
end
