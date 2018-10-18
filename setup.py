#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install

with open('README.rst', 'r') as f:
    readme = f.read()


class PycurlInstall(install):
    def run(self):
        if os.system('curl --version | grep NSS 2>/dev/null') != 0:
            os.environ['PYCURL_SSL_LIBRARY'] = 'openssl'
            os.system(
                'pip install --compile --install-option="--with-openssl" '
                'pycurl')
        else:
            os.environ['PYCURL_SSL_LIBRARY'] = 'nss'
            os.system(
                'pip install --compile --install-option="--with-nss" pycurl')
        install.run(self)

setup(
    name='automation_tools',
    version='0.1.0',
    description='Tools to help automating testing Foreman with Robottelo.',
    long_description=readme,
    author=u'Elyézer Rezende',
    author_email='erezende@redhat.com',
    url='https://github.com/SatelliteQE/automation-tools',
    cmdclass=dict(install=PycurlInstall),
    packages=['automation_tools', 'automation_tools/satellite6'],
    package_data={'': ['LICENSE']},
    package_dir={'automation_tools': 'automation_tools'},
    include_package_data=True,
    install_requires=[
        'beautifulsoup4',
        'Fabric3',
        'lxml',
        'pytest',
        'python-bugzilla==1.2.2',
        'requests',
        'robozilla',
        'six',
        'unittest2',
        'PyNaCl==1.2.1'
    ],
    license='GNU GPL v3.0',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ),
)
