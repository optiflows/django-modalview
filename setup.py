# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


install_reqs = parse_requirements('requirements.txt', session='dummy')
reqs = [str(ir.req) for ir in install_reqs]

try:
    with open('VERSION.txt', 'r') as v:
        version = v.read().strip()
except IOError:
    version = '0.0.0.dev0'


setup(
    name='django-modalview',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='Django app to add generic views.',
    url='https://github.com/optiflows/django-modalview',
    author='Enovacom Surycat',
    author_email='rand@surycat.com',
    install_requires=reqs,
    setup_requires=['setuptools_git>=1.0'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 1.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
