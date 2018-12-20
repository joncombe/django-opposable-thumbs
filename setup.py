# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-opposable-thumbs',
    version='0.0.1',
    author=u'Jon Combe',
    author_email='jon@naremit.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    url='https://naremit.com',
    license='BSD licence, see LICENCE file',
    description='Easy image manipulation for Django',
    zip_safe=False,
)
