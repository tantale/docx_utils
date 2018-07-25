========
Overview
========

.. start-badges

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/tantale/docx_utils/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/tantale/docx_utils/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/docx-utils.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/docx-utils

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/docx-utils.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/docx-utils

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/docx-utils.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/docx-utils


.. end-badges

Creation and manipulation of Open XML documents (mainly docx).

* Free software: MIT license


Features
========

This library allow you to:

* Convert Open XML documents into flat OPC format.


Installation
============

::

    pip install docx-utils


Documentation
=============

https://docx_utils.readthedocs.io/


Development
===========

To run the all tests run::

    tox

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

