# coding: utf-8
"""
Command line interface (CLI)
============================

Overview
--------

This module defines the main command line interface (CLI).
"""
import sys

import click

import docx_utils
import docx_utils.flatten
import docx_utils.emboss
import docx_utils.exceptions


@click.group(context_settings=(dict(terminal_width=120)))
@click.version_option(docx_utils.__version__)
def main():
    """Docx utilities"""


# fmt: off
@main.command(context_settings=(dict(terminal_width=120)))
@click.argument(
    "src_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False)
)
@click.argument(
    "dst_path",
    type=click.Path(exists=False, file_okay=True, dir_okay=False)
)
@click.option(
    "--on-error",
    type=click.Choice(["ignore", "strict"]),
    default="ignore",
    help="Control the way errors are handled when a part URI cannot be resolved",
)
@click.version_option(docx_utils.__version__)
# fmt: on
def flatten(src_path, dst_path, on_error):
    """
    Convert Open XML document to flat OPC format.

    \b
    src_path  Microsoft Office document to convert (.docx, .xlsx, .pptx)
    dst_path  Microsoft Office document converted into flat OPC format (.xml)
    """
    click.echo(u"Converting '{0}' to flat XML...".format(src_path))
    try:
        docx_utils.flatten.opc_to_flat_opc(src_path, dst_path, on_error=on_error)
    except docx_utils.exceptions.DocxUtilsException as exc:
        click.echo(u"Conversion of '{0}' failed:".format(src_path), err=True)
        click.echo(str(exc), err=True)
        sys.exit(1)
    else:
        click.echo(u"Conversion done: '{0}'.".format(dst_path))


# fmt: off
@main.command(context_settings=(dict(terminal_width=120)))
@click.argument(
    "src_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False)
)
@click.argument(
    "dst_path",
    type=click.Path(exists=False, file_okay=True, dir_okay=False)
)
@click.version_option(docx_utils.__version__)
# fmt: on
def emboss(src_path, dst_path, on_error):
    """
    Convert a flat OPC file (a XML file) in Open XML document.

    \b
    src_path  Flat OPC file to convert into Open XML document (.xml)
    dst_path  Microsoft Office document (.docx, .xlsx, .pptx)
    """
    click.echo(u"Converting '{0}' to Microsoft Office document...".format(src_path))
    try:
        docx_utils.emboss.flat_opc_to_office(src_path, dst_path)
    except docx_utils.exceptions.DocxUtilsException as exc:
        click.echo(u"Conversion of '{0}' failed:".format(src_path), err=True)
        click.echo(str(exc), err=True)
        sys.exit(1)
    else:
        click.echo(u"Conversion done: '{0}'.".format(dst_path))
