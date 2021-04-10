#!/usr/bin/env python3

from setuptools import setup
from sys import version_info

assert version_info >= (3, 7, 0), "logbisect requires >= Python 3.7"
INSTALL_REQUIRES = ["click", "python-dateutil"]


setup(
    name="logbisect",
    version="1.0.0",
    description=("search huge log files quickly"),
    long_description="quickly search huge files containing lines with ordered timestamps using bisection",
    packages=["logbisect"],
    url="http://github.com/michaelnugent",
    author="Mike Nugent",
    author_email="michael@michaelnugent.org",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIRES,
    entry_points={"console_scripts": ["logbisect = logbisect.cli:begin"]},
)