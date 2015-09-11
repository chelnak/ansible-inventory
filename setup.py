from setuptools import setup

setup(
	name='ansibleinventory',
	version='0.2',
	py_modules=['ansibleinventory.ansibleinventory'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		ansible-inventory=ansibleinventory.ansibleinventory:cli
	''',
)
