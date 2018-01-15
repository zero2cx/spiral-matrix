#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# setup.py

from os import path
from setuptools import setup, find_packages

def readme(filename):
    with open(path.join(path.dirname(__file__), filename)) as file:
        README = file.read()
    return README

setup(
    name = 'spiral-matrix',
    version = '0.1a1',
    packages = find_packages(),
    description = 'Generate a square 2-d matrix with an outward-spiraling '
            'series of elements',
    long_description = readme('README.rst'),
    author = 'David Schenck',
    author_email = 'zero2cx@gmail.com',
    license='GPL3+',
    url = 'https://github.com/zero2cx/spiral-matrix',
    download_url = 'https://github.com/zero2cx/spiral-matrix/archive/v0.1a1.tar.gz',
    include_package_data = True,
    python_requires = '>=3',
    keywords = ['spiral-matrix', '2d-matrix', 'matrix', 'command-line'],
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Development Status :: 3 - Alpha'
    ],
)
