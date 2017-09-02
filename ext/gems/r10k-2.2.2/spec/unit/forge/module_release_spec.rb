require 'spec_helper'
require 'r10k/forge/module_release'
require 'r10k/util/exec_env'
require 'puppet_forge'

describe R10K::Forge::ModuleRelease do
  subject { described_class.new('branan-eight_hundred', '8.0.0') }

  let(:forge_release_class) { PuppetForge::V3::Release }

  let(:download_path) { instance_double('Pathname') }
  let(:unpack_path) { instance_double('Pathname') }
  let(:target_dir) { instance_double('Pathname') }
  let(:file_lists) { {:valid=>['valid_ex'], :invalid=>[], :symlinks=>['symlink_ex']} }

  before do
    subject.download_path = download_path
    subject.unpack_path = unpack_path
  end

  describe '#download' do
    it "downloads the module from the forge into `download_path`" do
      expect(subject.forge_release).to receive(:download).with(download_path)
      subject.download
    end
  end

  describe '#verify' do
    it "verifies the module checksum based on the Forge file checksum" do
      allow(subject.forge_release).to receive(:data).and_return('file_md5' => 'something')
      expect(subject.forge_release).to receive(:verify).with(download_path)
      subject.verify
    end
  end

  describe '#unpack' do
    it "unpacks the module tarball in `download_path` into the provided target path" do
      expect(PuppetForge::Unpacker).to receive(:unpack).with(download_path.to_s, target_dir.to_s, unpack_path.to_s).\
          and_return({:valid=>["extractedmodule/metadata.json"], :invalid=>[], :symlinks=>[]})
      subject.unpack(target_dir)
    end

    it "raises an error if symlinks are present during the unpacking process after unpacking" do
      logger_dbl = double(Log4r::Logger)
      allow(subject).to receive(:logger).and_return(logger_dbl)
      expect(PuppetForge::Unpacker).to receive(:unpack).with(download_path.to_s, target_dir.to_s, unpack_path.to_s).\
          and_return(file_lists)
      expect(logger_dbl).to receive(:debug1)
      expect(logger_dbl).to receive(:debug2)
      expect {
        subject.unpack(target_dir)
      }.to raise_error(R10K::Error, "Symlinks are unsupported and were not unpacked from the module tarball. " +
                                    "#{subject.forge_release.slug} contained these ignored symlinks: #{file_lists[:symlinks]}")
    end
  end

  describe "#cleanup" do
    it "cleans up the download and unpack paths" do
      expect(subject).to receive(:cleanup_unpack_path)
      expect(subject).to receive(:cleanup_download_path)
      subject.cleanup
    end
  end

  describe "#cleanup_unpack_path" do
    it "ignores the unpack_path if it doesn't exist" do
      expect(unpack_path).to receive(:exist?).and_return false
      expect(unpack_path).to_not receive(:rmtree)
      subject.cleanup_unpack_path
    end

    it "removes the unpack_path if it exists" do
      expect(unpack_path).to receive(:exist?).and_return true
      expect(unpack_path).to receive(:rmtree)
      subject.cleanup_unpack_path
    end
  end

  describe "#cleanup_download_path" do
    it "ignores the download_path if it doesn't exist" do
      expect(download_path).to receive(:exist?).and_return false
      expect(download_path).to_not receive(:delete)
      subject.cleanup_download_path
    end

    it "removes the download_path if it exists" do
      expect(download_path).to receive(:exist?).and_return true
      expect(download_path).to receive(:delete)
      subject.cleanup_download_path
    end
  end

  describe '#install' do
    it "performs all steps needed to install the module" do
      expect(subject).to receive(:download)
      expect(subject).to receive(:verify)
      expect(subject).to receive(:unpack).with(target_dir)
      expect(subject).to receive(:cleanup)
      subject.install(target_dir)
    end
  end
end
