=========
Changelog
=========

.. start-exclude

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

.. end-exclude

v0.1.3 (unreleased)
===================

Fixed
~~~~~


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
