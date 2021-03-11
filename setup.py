from setuptools import setup, find_packages

setup(
	name='djando',
	version='0.2',
	description='Using Docker with Django made easy',
	url='http://github.com/rayronvictor/djando',
	author='Rayron Victor',
	author_email='rayronvictor@gmail.com',
	license='MIT',
	include_package_data=True,
	packages=find_packages(),
	scripts=['bin/djando'],
	entry_points={
		'console_scripts': [
			'djandoinit=djando.command_line:main'
		],
	},
	zip_safe=False
)
