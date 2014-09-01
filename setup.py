#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup

with codecs.open(
    os.path.join(os.path.dirname(__file__), 'README.rst'), 'r', 'utf8',
) as ld_file:
    long_description = ld_file.read()


setup (
    name = 'doit-cmd',
    version = '0.1.0',
    author = 'Eduardo Naufel Schettino',
    author_email = 'schettino72@gmail.com',
    description = 'Helper to create doit tasks that execute a command',
    long_description = long_description,
    url = 'https://github.com/pydoit/doit-cmd/',
    keywords = ['doit',],
    platforms = ['any'],
    license = 'MIT',
    py_modules = ['doitcmd'],
    install_requires = ['doit'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
