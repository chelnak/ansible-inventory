#Welcome to ansibleinventory

This is a script that can be used to manage your ansible inventory. It assumes
that you are using a file per host configuration.

For example:

You have a folder called /etc/ansible/hosts which contains a file per host you wish to
manage with ansible.

```
ls /etc/ansible/hosts
host1.domain.com
host2.domain.com
```

Host files are formatted in the following way:

```
[role]
host1.domain.com
```

#Installation
Install by running:

```
python setup.py install
```

For testing purposes you can also run this in a virtualenv.

#Usage

If not specified on either command the --inventory switch will default to /etc/ansible/hosts

###Adding a new host

```
ansible-inventory add --role 'test-role' --hostname 'myhost.company.com' --inventory '/etc/ansible/hosts'
```

###Removing a host

```
ansible-inventory remove --hostname 'myhost.company.com' --inventory '/etc/ansible/hosts'
```

#Removal

To uninstall ansiibleinventory you can run:

```
pip uninstall ansibleinventory
```
