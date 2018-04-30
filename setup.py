import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='qbuild',
    version='0.0.2',
    description='A build system for our technology challenges',
    long_description=README,
    author='Mohammad Javad Naderi',
    url='https://gitlab.com/codamooz/challenges/qbuild',
    packages=find_packages(),
    include_package_data=True,
    scripts=['qbuild/qbuild'],
    install_requires=[
        'sh',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
