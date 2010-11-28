#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R. Lucindo (lucindo@gmail.com)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1'

sdict = {
    'name' : 'konig',
    'version' : version,
    'description' : 'Simple Distributed Graph Database',
    'long_description' : 'Simple Distributed Graph Database (redis based)',
    'url': 'http://github.com/lucindo/konig',
    'download_url' : 'http://cloud.github.com/downloads/lucindo/konig/konig-%s.tar.gz' % version,
    'author' : 'Renato Lucindo',
    'author_email' : 'lucindo@gmail.com',
    'keywords' : ['Graph', 'Database', 'Distributed', 'Redis'],
    'license' : 'BOLA',
    'packages' : ['konig'],
    'test_suite' : 'test.run_tests',
    }

setup(**sdict)
