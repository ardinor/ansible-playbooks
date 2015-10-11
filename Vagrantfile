# -*- mode: ruby -*-

# http://hakunin.com/six-ansible-practices
require_relative './.vagrant/key_authorization'

Vagrant.configure(2) do |config|

  config.vm.box = "centos/7"

  authorize_key_for_root config, '~/.ssh/deploy.pub'

  config.vm.define :test_vm do |test_vm|
    test_vm.vm.network 'private_network', ip: '192.168.33.10'
    test_vm.vm.hostname = "test.defestri.dev"
  end

end
