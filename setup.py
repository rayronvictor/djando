from setuptools import setup, find_packages

setup(
	name='djando',
	version='0.1',
	description='Using Docker with Django made easy',
	url='http://github.com/rayronvictor/djando',
	author='Rayron Victor',
	author_email='rayronvictor@gmail.com',
	license='MIT',
	include_package_data=True,
	packages=find_packages(),
	package_dir={'djando': 'djando'},
	package_data={
		'djando': ['data']
	},
	scripts=['bin/djando'],
	entry_points={
		'console_scripts': [
			'djandoinit=djando.command_line:main'
		],
	},
	zip_safe=False
)
