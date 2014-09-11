__author__= 'Dawson Reid'

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import os


def parse_packages(package_file, packages=[]):
    with open(package_file, 'r') as f:
        for line in f:
            packages.append(line.rstrip())
    return packages

install_packages = parse_packages('requirements.txt')
#print(install_packages)

f = open('README.md', 'r')
README = f.read()
f.close()

class PyTest(TestCommand):
  '''
  '''
  user_options = []

  def finalize_options(self):
    TestCommand.finalize_options(self)
    self.test_args = [
      'tests/test_private.py'
    ]
    self.test_suite = True

  def run_tests(self):
    import pytest
    sys.path.insert(0, os.path.dirname(__file__))
    errno = pytest.main(self.test_args)
    sys.exit(errno)


setup(name='cavirtex-sdk',
      version='0.1.001',
      description=README,
      packages=find_packages(),
      install_requires=install_packages,
      test_require=['pytest'],
      cmdclass={
          'test': PyTest
      })
