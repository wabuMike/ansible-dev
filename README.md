ansible-dev
=========

An Ansible role to setup an Ansible development environment on a host.

The motiviation of writing this role was to have a development environment built with Vagrant, which in turn can run this role to setup ansible + molecule.

Molecule is installed into a virtual environment (virtualenv) at /opt/virtenv/molecule. Use `source /opt/virtenv/molecule/bin/activate` to activate it.

I'll give an example on how to do this once I'm finished.

After creating this role, I found out that it's pretty useless to build a remote development environment when half of the development tools is needed on the host to build this development environment. 

Requirements
------------

* Ansible installed on your host
* Currently works only with Ubuntu running on the remote machine.

Role Variables
--------------

* there are currently no role variables

Dependencies
------------

* none

Example Playbook
----------------

TODO

License
-------

GPLv3

Author Information
------------------

wabuMike (https://fosstodon.org/@WabuMike)
