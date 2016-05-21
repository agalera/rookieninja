#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from glob import glob
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

readme = read_md('README.md')
changelog = read_md('CHANGELOG.md')

setup(
    name='rookieninja',
    version='0.0.2',
    description='',
    long_description=readme + '\n\n' + changelog,
    author='Alberto Galera Jimenez',
    author_email='galerajimenez@gmail.com',
    url='https://github.com/kianxineki/rookieninja',
    # packages=['rookieninja', 'rookieninja.models', 'rookieninja.modules',
    #           'rookieninja.routines', 'rookieninja.scripts',
    #           'rookieninja.views'],
    packages=find_packages(),
    data_files=[('', glob('*.md')),
                ('static', glob('static/*.???')),
                ('static/imgs', glob('static/imgs/*.???')),
                ('static/templates', glob('static/templates/*.???')),
                ],
    include_package_data=True,
    install_requires=['requests', 'bottle', 'jinja2', 'meinheld'],
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
