#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip.req import parse_requirements
from pip.download import PipSession
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()


def get_requirements(filepath):
    analysis = parse_requirements(filepath, session=PipSession())
    return [str(requirement.req) for requirement in analysis]

requirements = get_requirements('requirements.txt')
test_requirements = get_requirements('testing_requirements.txt')

setup(
    name='namegenerator',
    version='0.1.2',
    description="A name generation program",
    long_description=readme + '\n\n' + changelog,
    author="Jeffery Tillotson",
    author_email='jpt@jeffx.com',
    url='https://github.com/jeffx/namegenerator',
    packages=[
        'names',
        'wordlist'
    ],
    package_dir={'names': 'names'},
    package_data={'': ['data/words.dat']},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='namegenerator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'namegen = names.cli:cli'
        ]
    }
)