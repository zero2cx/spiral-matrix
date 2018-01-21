#!/usr/bin/env python
# encoding: utf-8
# vim: set ff=unix fenc=utf-8 et ts=4 sts=4 sta sw=4:
#
# setup.py

import os
from setuptools import setup, find_packages

def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        readme = file.read()
    return readme

setup(
    name = 'spiral-matrix',
    version = '0.1.4',
    packages = find_packages(),
    description = 'Generate a square 2-d matrix with an outward-spiraling '
            'series of elements',
    long_description = read('README.rst'),
    entry_points = {
        'console_scripts': ['spiral-matrix = spiral_matrix.spiral_matrix:main'],
    },
    author = 'David Schenck',
    author_email = 'zero2cx@gmail.com',
    license='GPL3+',
    url = 'https://github.com/zero2cx/spiral-matrix',
    include_package_data = True,
    python_requires = '>=3',
    keywords = [
        'spiral-matrix',
        '2d-matrix',
        'matrix',
        'command-line',
        'console',
    ],
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Development Status :: 4 - Beta',
    ],
)
