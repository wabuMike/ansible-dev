import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ansible_installed(host):
    ansible = host.package('ansible')

    assert ansible.is_installed


def test_virtualenv_installed(host):
    packages = host.pip_package.get_packages(pip_path='~/molecule/bin/pip')

    assert "molecule" in packages
