# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='lirix',
    version='0.1.0',
    description='lirix',
    long_description=readme,
    author='Xade',
    author_email='git@xade.eu',
    url='https://github.com/x4d3/lirix',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

