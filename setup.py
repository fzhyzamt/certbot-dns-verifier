#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

__version__ = '0.0.1'
__author__ = 'fzhyzamt'
__email__ = 'fzhyzamt@163.com'
__url__ = 'https://github.com/fzhyzamt/certbot-dns-verifier'

install_requires = [
    'certbot',
    'zope.interface',
    'dns-lexicon'
]
docs_extras = [
    'Sphinx>=1.0',  # autodoc_member_order = 'bysource', autodoc_default_flags
    'sphinx_rtd_theme',
]

setup(
    name='certbot-dns-verifier',
    package=find_packages(),
    entry_points={
        'certbot.plugins': [
            'dns-dnspod = certbot_dns_verifier.dns_verifier:Authenticator',
            # 'verifier_installer = certbot_dns_verifier.dns_dnspod:Installer',
        ],
    },
    version=__version__,
    description="DNS verifier plugin for certbot",
    # long_description=readme,
    author=__author__,
    author_email=__email__,
    url=__url__,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(exclude=['docs', 'examples', 'tests', 'venv']),
    include_package_data=True,
    test_suite="certbot_dns_verifier",
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=install_requires,
    extras_require={
        'docs': docs_extras,
    },
    # tests_require=["pytest"]
)
