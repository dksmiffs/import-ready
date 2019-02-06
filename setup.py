from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
   name='importable',
   version='0.3.0',
   description='A simple importable Python package',
   long_description=long_description,
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

