#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of jupyter-samples.
# https://github.com/garaemon/jupyter-samples

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, garaemon <garaemon@gmail.com>

from setuptools import setup, find_packages
from jupyter_samples import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='jupyter-samples',
    version=__version__,
    description='Jupyter samples',
    long_description='''
Jupyter samples
''',
    keywords='',
    author='garaemon',
    author_email='garaemon@gmail.com',
    url='https://github.com/garaemon/jupyter-samples',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'jupyter-samples=jupyter_samples.cli:main',
        ],
    },
)
