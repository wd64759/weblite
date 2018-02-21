from setuptools import setup

setup(
    name='weblite',
    version='0.0.1',
    packages=['weblite'],
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy'
    ],
)
