#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'Max Arnold <arnold.maxim@gmail.com>'
__version__ = '0.1.0'

setup(
    name='devpi-slack',
    version=__version__,

    # Package dependencies.

    # Metadata for PyPI.
    author='Max Arnold',
    author_email='arnold.maxim@gmail.com',
    license='BSD',
    url='http://github.com/innoteq/devpi-slack',
    keywords='devpi slack notification',
    description='Devpi plugin for sending Slack channel notifications',
    long_description=open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.md')), 'r').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: System Administrators",
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ],
    packages=['devpi_slack'],
    entry_points={
        'devpi_server': [
            "devpi-slack = devpi_slack.main"]},
    install_requires=['devpi-server>=2.3.0'],
    platforms='any',
)
