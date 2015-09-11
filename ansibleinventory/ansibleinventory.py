#!/usr/bin/python
import click
import os

from sys import exit


def getHostFile(inventory, hostname):

    if not inventory.endswith('/'):
        inventory = inventory + '/'

    hostFile = "{inventory}{hostname}".format(inventory=inventory,
                                              hostname=hostname)

    return hostFile


@click.group()
def cli1():
    pass


@cli1.command()
@click.option('--role', required=1, help='Ansible role')
@click.option('--hostname',
              required=1,
              help='Hostname of the server to add to the inventory')
@click.option('--hostaddress',
	      required=1,
	      help='IP address of the server to add to the inventory')
@click.option('--inventory',
              default='/etc/ansible/hosts',
              help='Ansible inventory folder')
def add(role, hostname, hostaddress, inventory):

    hostFile = getHostFile(inventory, hostname)

    try:
        with open(hostFile, 'w') as f:

            f.write('[{role}]\n'.format(role=role))
	    f.write('{hostname} ansible_ssh_host={hostaddress}'.format(hostname=hostname, hostaddress=hostaddress))

        click.echo('Host file created at {hostFile} with role: {role}'.format(
            hostFile=hostFile,
            role=role))

    except OSError as e:

        click.echo('An error occured: {error}'.format(error=e))


@click.group()
def cli2():
    pass


@cli2.command()
@click.option('--hostname',
              required=1,
              help='Hostname of the server to add to the inventory')
@click.option('--inventory',
              default='/etc/ansible/hosts',
              help='Ansible inventory folder')
def remove(hostname, inventory):

    hostFile = getHostFile(inventory, hostname)

    try:
        os.remove(hostFile)
        click.echo('Host file removed successfully.')

    except OSError as e:

        click.echo('An error occured: {error}'.format(hostFile=hostFile,
                                                      error=e))


cli = click.CommandCollection(sources=[cli1, cli2])

if __name__ == '__main__':
    cli()
