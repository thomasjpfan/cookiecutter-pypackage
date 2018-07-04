#!/usr/bin/env python

import os

from codecs import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requirements = []

with open('VERSION', 'r') as f:
    version = f.read().rstrip()

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='{{cookiecutter.github_repo}}',
    version=version,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.5',
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
