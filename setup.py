from setuptools import setup

setup(
	name='weblite',
	package=['weblite'],
	include_package_date=True,
	install_requires=[
		'flask',
	],
	setup_requires=[
		'pytest-runner',
	],
	tests_require=[
		'pytest',
	],
)