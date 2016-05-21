#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found")
    read_md = lambda f: open(f, 'r').read()


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


try:
    readme = read_md('README.md')
except:
    readme = ""
try:
    changelog = read_md('CHANGELOG.md')
except:
    changelog = ""

setup(
    name='rookieninja',
    version='0.1.1',
    description='Displays information about your fellow fleet',
    long_description=readme + '\n\n' + changelog,
    author='Alberto Galera Jimenez',
    author_email='galerajimenez@gmail.com',
    url='https://github.com/kianxineki/rookieninja',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pymongo', 'requests', 'bottle', 'jinja2', 'meinheld'],
    license="GPL",
    zip_safe=False,
    keywords='rookieninja, eve, online',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'server_rookieninja = rookieninja.server:main'
        ]
    },
)
