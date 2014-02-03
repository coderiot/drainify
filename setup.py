#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='drainify',
    version='0.1',
    license='GPL',
    description='Recording spotify\'s stream.',
    author='peterr',
    author_email='coderiot@zoho.com',
    url='https://github.com/coderiot/drainify/',
    install_requires=['dbus', 'eyed3', 'gobject'],
    packages=['drainify', ],
)
