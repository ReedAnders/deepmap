# Copyright (C) 2016 Reed Anderson.
# From: https://github.com/ReedAnders/deepmap
# License: MIT BY https://opensource.org/licenses/MIT

from setuptools import setup, find_packages

setup(name='deepmap',
      version='0.1.0',
      packages=['DeepMap'],
      entry_points={
          'console_scripts': [
              'deepmap = deepmap.__main__:main'
          ]
      },
      test_suite = 'test',
      )
