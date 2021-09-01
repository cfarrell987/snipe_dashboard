from setuptools import setup, find_packages
import sys
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = sys.version_info[:2]
if version < (3, 9):
    print('Snipe Dashboard requires Python version 3.9 or later' +
          ' ({}.{}) detected.'.format(*version))
    sys.exit(-1)

VERSION = '0.1.0'

install_requires = ['requests']

setup(name='Snipe Dashboard',
      version=VERSION,
      description='A SnipeIT Dashboard using SnipeIT\'s REST API ',
      long_description=long_description,
      author='Caleb Farrell',
      author_email='caleb.farrell@valhallahosting.ca',
      url='https://github.com/cfarrell987/snipe_dashboard',
      license='GPLv3',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      entry_points={'console_scripts': ['absd = dashboard.main:main']})
