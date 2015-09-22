#!/usr/bin/env python

import os
import sys

from setuptools import setup


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

install_requires = [
    'ujson>=1.33',
    'wheezy.core>=0.1.140',
    'wheezy.caching>=0.1.114',
    'wheezy.html>=0.1.147',
    'wheezy.http>=0.1.340',
    'wheezy.routing>=0.1.157',
    'wheezy.security>=0.1.64',
    'wheezy.template>=0.1.167',
    'wheezy.validation>=0.1.135',
    'wheezy.web>=0.1.485'
]

install_optional = [
    'pycrypto>=2.6.1'
]

if sys.version_info[0] == 2:
    install_optional.append('pylibmc>=1.2.3')

install_requires += install_optional

try:
    import uuid  # noqa
except ImportError:
    install_requires.append('uuid')

dependency_links = [
    # pylibmc
    'https://bitbucket.org/akorn/wheezy.caching/downloads',
    # pycrypto
    'https://bitbucket.org/akorn/wheezy.security/downloads'
]

setup(
    name='mysite',
    version='0.1',
    description='MySite Project',
    long_description=README,
    url='https://scm.dev.local/svn/mysite/trunk',

    author='MySite Team',
    author_email='mysite at dev.local',

    license='COMMERCIAL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=[
        'public',
        'public.web'
    ],
    package_dir={'': 'src'},

    zip_safe=False,
    install_requires=install_requires,
    dependency_links=dependency_links,
    extras_require={
    },

    platforms='any'
)
