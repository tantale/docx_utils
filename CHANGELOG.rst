=========
Changelog
=========

.. start-exclude

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

.. end-exclude

v0.2.0 (unreleased)
===================


v0.1.4 (unreleased)
===================


v0.1.3 (2020-07-15)
===================

Fixed
~~~~~

* Correct the project's dependencies: Enum34 is only required for Python versions < 3.4.

* Add the :mod:`~docx_utils.exceptions` module: Exception hierarchy for the docx-utils package.

* Fix `#1 <https://github.com/tantale/docx_utils/issues/1>`_:

  - Add the *on_error* option in the :func:`~docx_utils.flatten.opc_to_flat_opc` function
    in order to ignore (or raise an exception) when a part URI cannot be resolved
    during the Microsoft Office document parsing.

  - Change the command line interface: add the ``--on-error`` option to handle parsing error.

Other
~~~~~

* Continuous Integration: add configurations for Python 3.7 and Python 3.8.


v0.1.2 (2018-07-26)
===================

Fixed
~~~~~

* Drop support for PyPy: it seams that lxml is not available for this Python implementation.

* Drop support for Python 3.7: this Python version is not yet available on all platform.
  However, it is known to work on Ubuntu with the python-3.7-dev release.

Other
~~~~~

* Use the pseudo-tags ``start-exclude``/``end-exclude`` in ``CHANGELOG.rst`` and ``README.rst``
  to exclude text from the generated ``PKG-INFO`` during setup.


v0.1.1 (2018-07-25)
===================

Fixed
~~~~~

* Fix wheel version on PyPi.


v0.1.1 (2018-07-24)
===================

Added
~~~~~

* First release.
