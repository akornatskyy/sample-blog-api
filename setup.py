#!/usr/bin/env python

import os

from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

install_requires = [
    'ujson',
    'pycryptodome',
    'wheezy.core',
    'wheezy.caching',
    'wheezy.html',
    'wheezy.http',
    'wheezy.routing',
    'wheezy.security',
    'wheezy.template',
    'wheezy.validation',
    'wheezy.web'
]

setup(
    name='sample-blog-api',
    version='0.1',
    description='Sample Blog API',
    long_description=README,
    url='https://github.com/akornatskyy/sample-blog-api',
    author='Andriy Kornatskyy',
    author_email='andriy.kornatskyy@live.com',
    license='COMMERCIAL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        'membership',
        'membership.repository',
        'membership.service',
        'membership.web',
        'posts',
        'posts.repository',
        'posts.service',
        'posts.web',
        'public',
        'public.repository',
        'public.service',
        'public.web',
        'shared'
    ],
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=install_requires,
    platforms='any'
)
