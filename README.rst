========
Overview
========

.. start-exclude

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/docx_utils/badge/?style=flat
    :target: https://readthedocs.org/projects/docx_utils
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/tantale/docx_utils.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/tantale/docx_utils

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/tantale/docx_utils?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/tantale/docx_utils

.. |requires| image:: https://requires.io/github/tantale/docx_utils/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/tantale/docx_utils/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/tantale/docx_utils/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/tantale/docx_utils

.. |version| image:: https://img.shields.io/pypi/v/docx-utils.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/docx-utils

.. |commits-since| image:: https://img.shields.io/github/commits-since/tantale/docx_utils/v0.1.2.svg
    :alt: Commits since latest release
    :target: https://github.com/tantale/docx_utils/compare/v0.1.2...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/docx-utils.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/docx-utils

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/docx-utils.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/docx-utils

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/docx-utils.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/docx-utils


.. end-exclude

Creation and manipulation of Open XML documents (mainly docx).

* Free software: MIT license


Features
========

This library allow you to:

* Convert Open XML documents into flat OPC format.


Installation
============

.. code:: bash

    pip install docx-utils


Using the library
=================

Using the library to convert an Open XML document into flat OPC format:

.. code:: python

   >>> from docx_utils.flatten import opc_to_flat_opc
   >>> opc_to_flat_opc("sample.docx", "sample.xml")


Command Line Interface (CLI)
============================

Printing the online help:

.. code:: bash

   $ docx_utils --help
   Usage: docx_utils [OPTIONS] COMMAND [ARGS]...

     Docx utilities

   Options:
     --version  Show the version and exit.
     --help     Show this message and exit.

   Commands:
     flatten  Convert an Open XML document into flat OPC format.

Converting an Open XML document into flat OPC format:

.. code:: bash

   $ docx_utils flatten sample.docx sample.xml
   Converting 'sample.docx' to flat XML...
   Conversion done: 'sample.xml'.


Documentation
=============

https://docx_utils.readthedocs.io/


Development
===========

To run the all tests run::

    tox

.. start-exclude

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

.. end-exclude
