# coding: utf-8
from __future__ import print_function

import subprocess
import sys

import docx_utils


def test_main():
    # can call __main__ with 'python -m docx_utils'
    python = sys.executable
    args = [python, '-m', 'docx_utils', '--version']
    output = subprocess.check_output(args)
    output = output.decode(sys.getfilesystemencoding())
    assert output.strip() == u'__main__.py, version {0}'.format(docx_utils.__version__)


def test_main__import():
    import docx_utils.__main__ as main_module
    assert hasattr(main_module, 'main')
