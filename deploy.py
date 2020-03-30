#!/usr/bin/env python
from deployer.client import start
from deployer.host import SSHHost
from deployer.node import Node
from deployer.utils import esc1


class remote_host(SSHHost):
    address = 'ssh.xala.no'
    username = 'xala.no'
    password = 'Xala@@2019!'
    key_filename = None


class DjangoDeployment(Node):
    class Hosts:
        host = remote_host

    project_directory = '~/git/rtamediahub'
    repository = 'git@github.com:xalatech/rtamediahub.git'

    def install_git(self):
        """ Installs the ``git`` package. """
        self.host.sudo('apt-get install git')

    def git_clone(self):
        """ Clone repository."""
        with self.host.cd(self.project_directory, expand=True):
            self.host.run("git clone '%s'" % esc1(self.repository))

    def git_checkout(self, commit):
        """ Checkout specific commit (after cloning)."""
        with self.host.cd(self.project_directory, expand=True):
            self.host.run("git checkout '%s'" % esc1(commit))


if __name__ == '__main':
    start(DjangoDeployment)