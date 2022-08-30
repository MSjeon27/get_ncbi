#! /usr/bin/env python

from setuptools import setup, find_packages, Command

from distutils.command.build_py import build_py

setup(
    name             = 'get_ncbi',
    version          = '1.0.2',
    description      = 'Package for distribution',
    author           = 'msjeon27',
    author_email     = 'msjeon27@cau.ac.kr',
    url              = '',
    download_url     = '',
    install_requires = ['argparse', 'bs4'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GETNCBI', 'getncbi'],
    cmdclass         = {'build_py': build_py},
	scripts          = ['scripts/get_ncbi'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 
