from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Swarm Class',
  ext_modules = cythonize("swarm.pyx"),
)
