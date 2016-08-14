from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Schaffers F6 function',
  ext_modules = cythonize("f6.pyx"),
)
