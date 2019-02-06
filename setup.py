"""
Describe the importable module distribution to the Distutils, per the following:
    https://docs.python.org/3/distutils/setupscript.html
"""
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='importable',
    version='0.5.0',
    description='A simple importable Python package',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/dave.k.smith/importable',
    author='Dave Smith',
    author_email='dave.k.smith@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='import package huntsville havoc testpypi',
    packages=find_packages(),
)
