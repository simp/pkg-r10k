require 'git_utils'
require 'r10k_utils'
require 'master_manipulator'
test_name 'CODEMGMT-90 - C63462 - Specify Invalid Command-line Environment Flag'

#Init
git_environments_path = '/root/environments'
last_commit = git_last_commit(master, git_environments_path)
r10k_fqp = get_r10k_fqp(master)

#Verification
error_message_regex = /environment: illegal option/

#Teardown
teardown do
  clean_up_r10k(master, last_commit, git_environments_path)
end

#Tests
step 'Attempt to Deploy via r10k'
on(master, "#{r10k_fqp} deploy environment -x", :acceptable_exit_codes => 1) do |result|
  assert_match(error_message_regex, result.stderr, 'Expected message not found!')
end
