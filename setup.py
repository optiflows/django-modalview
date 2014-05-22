import os
from setuptools import setup, find_packages


def README():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except (IOError, ImportError):
        return open('README.md').read()

setup(
    name='django-modalview',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='Apache License 2.0',
    description='Django app to add generic views.',
    long_description=README(),
    url='https://github.com/optiflows/django-modalview',
    author='Valentin Monte',
    author_email='valentin.monte@optiflows.com',
    install_requires=[
        'django>=1.5',
    ],
    setup_requires=[
        'setuptools_git>=1.0',
        'pypandoc',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
