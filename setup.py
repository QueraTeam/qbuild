import os
from qbuild import version
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='qbuild',
    version=version.__version__,
    description='A build system for our technology challenges',
    long_description=README,
    author='Mohammad Javad Naderi',
    url='https://gitlab.com/codamooz/challenges/qbuild',
    packages=find_packages(),
    include_package_data=True,
    scripts=['qbuild/qbuild', 'qbuild/qbuild_diff-so-fancy'],
    install_requires=[
        'sh',
        'Jinja2',
        'qbuild-jupyter @ git+https://github.com/peynaj/qbuild-jupyter',
        # TODO: switch to 'git+https://gitlab.com/codamooz/challenges/qbuild-jupyter' ;
        #       if this repos is completed and you have access to it.
        # TODO: How to define version of qbuild-jupyter to install: '0.1.2'
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
