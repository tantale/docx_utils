# coding: utf-8
"""
Command line interface (CLI)
============================

Overview
--------

This module defines the main command line interface (CLI).
"""

import click

import docx_utils
import docx_utils.flatten


@click.group(context_settings=(dict(terminal_width=120)))
@click.version_option(docx_utils.__version__)
def main():
    """Docx utilities"""


@main.command(context_settings=(dict(terminal_width=120)))
@click.argument('src_path', type=click.Path(exists=True, file_okay=True, dir_okay=False))
@click.argument('dst_path', type=click.Path(exists=False, file_okay=True, dir_okay=False))
@click.version_option(docx_utils.__version__)
def flatten(src_path, dst_path):
    """
    Convert Open XML document to flat OPC format.

    \b
    src_path  Microsoft Office document to convert (.docx, .xlsx, .pptx)
    dst_path  Microsoft Office document converted into flat OPC format (.xml)
    """
    click.echo(u"Converting '{0}' to flat XML...".format(src_path))
    docx_utils.flatten.opc_to_flat_opc(src_path, dst_path)
    click.echo(u"Conversion done: '{0}'.".format(dst_path))
