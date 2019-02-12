#!/usr/bin/env python
""" Package setup /install and metadata for lambdata
"""

import setuptools

REQUIRED = [
    "numpy", 
    "pandas"
]

with open("Readme.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lamdata-hughjafro",
    version="0.0.1",
    author="hughjafro",
    description="A collection of Data Science helper functions",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/hughjafro/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
