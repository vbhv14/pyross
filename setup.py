import numpy
import os, sys, os.path, tempfile, subprocess, shutil
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True


#here openMP support is not opted, which can be changed to ['-fopenmp'] .
ompArgs = None 


setup(
    name='pyross',
    version='1.0.0',
    url='https://gitlab.com/rajeshrinet/pyross',
    author='The pyross team',
    license='MIT',
    description='python library for numerical simulation of infectious disease',
    long_description='pyross is a library for numerical simulation of infectious disease',
    platforms='tested on LINUX',
    ext_modules=cythonize([ Extension("pyross/*", ["pyross/*.pyx"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=ompArgs,
        extra_link_args=ompArgs 
        )]),
    libraries=[],
    packages=['pyross'],
    package_data={'pyross': ['*.pxd']}
)


