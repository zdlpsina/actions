import os
from setuptools import setup,find_namespace_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys

__version__ = "0.0.1"
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
ext_modules = [
    Pybind11Extension("mathop",
        ["op.cpp"],
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        ),
]
setup(
    name = "mathop",
    version = __version__,
    author = "zdl",
    author_email = "zdlp@sina.cn",
    description = ("An demonstration of how to create, document package"),
    license = "BSD",
    keywords = "mathop",
    url = "http://8.142.61.226/wiki/%E5%B7%A5%E4%BD%9C/%E9%9D%92%E6%A4%92%E5%AE%9E%E4%B9%A0/%E6%89%93%E5%8C%85/python_package/python_package/",
    packages=find_namespace_packages(include=['mathop.*']),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],

    ext_modules=ext_modules,
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)

