# coding: utf-8

try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib

PROJECT_DIR = pathlib.Path(__file__).absolute().parent.parent
