#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# setup.py

from setuptools import setup, find_packages

setup(
    name = 'SpiralMatrix',
    version = '0.1',
    packages = find_packages(),
    description = 'Construct a square 2-d matrix with an outward-spiraling '
            'series of elements.',
    author = 'David Schenck',
    author_email = 'zero2cx@gmail.com',
    url = 'https://github.com/zero2cx/spiral-matrix',
    download_url = 'https://github.com/zero2cx/spiral-matrix/archive/0.1.tar.gz',
    keywords = ['spiral-matrix', '2d-matrix', 'matrix', 'command-line'],
    classifiers = [],
)
