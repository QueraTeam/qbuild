import os
from qbuild import version
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r", encoding="UTF-8") as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="qbuild",
    version=version.__version__,
    description="A build system for Quera technology challenges",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Quera Team",
    url="https://github.com/QueraTeam/qbuild",
    packages=find_packages(),
    include_package_data=True,
    scripts=["qbuild/qbuild", "qbuild/qbuild_diff-so-fancy"],
    install_requires=["sh", "Jinja2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
    ],
)
