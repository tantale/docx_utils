#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
import os
import re

from setuptools import find_packages
from setuptools import setup

install_requires = [
    # Open source libraries
    "click",
    "six",
    "lxml",
    'enum34 ; python_version < "3.4"',
]

with io.open("tests/requirements.txt") as fd:
    tests_require = [line.strip() for line in fd if line.strip() and not line.startswith("#")]

dev_require = [
    "tox < 4",
    "zipp < 2 ; python_version < '3'",
    "configparser < 5 ; python_version < '3'",
    "virtualenv < 20 ; python_version < '3' and sys_platform == 'win32'",
]

extras_require = {"test": tests_require, "dev": dev_require}


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        text = fd.read()
        text = re.sub(
            text_type(r":[a-z]+:`~?(.*?)`"),
            text_type(r"``\1``"),
            text,
            flags=re.M | re.S,
        )
        text = re.sub(
            text_type("^.. start-exclude.*?^.. end-exclude"),
            text_type(""),
            text,
            flags=re.M | re.S,
        )
        return text


setup(
    # --- identity
    name="docx-utils",
    version="0.1.4",
    # --- description
    description="Creation and manipulation of Open XML documents (mainly docx).",
    long_description=u"{0}\n{1}".format(read("README.rst"), read("CHANGELOG.rst")),
    long_description_content_type="text/x-rst",
    author="Laurent LAPORTE",
    author_email="tantale.solutions@gmail.com",
    url="https://github.com/tantale/docx_utils",
    license="MIT License",
    platforms=["posix", "nt"],
    keywords="Microsoft, Office, Word, Excel, PowerPoint, docx, xlsx, pptx, XML",
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    # --- packaging
    install_requires=install_requires,
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    exclude_package_data={"docx_utils": []},
    zip_safe=False,
    extras_require=extras_require,
    entry_points={"console_scripts": ["docx_utils = docx_utils.cli:main"]},
    python_requires=">= 2.7, != 3.0.*, != 3.1.*, != 3.2.*, != 3.3.*, != 3.4.*, < 4",
)
