# coding: utf-8

from __future__ import absolute_import

import py
from tests import PROJECT_DIR

from docx_utils.flatten import opc_to_flat_opc


def test_opc_to_flat_opc(tmpdir):
    # type: (py.path.LocalPath) -> None
    relpath = 'tests/resources/test_opc_to_flat_opc/Sample document with table.docx'
    res_path = py.path.local(PROJECT_DIR).join(relpath)  # type: py.path.LocalPath
    src_path = tmpdir.join(res_path.basename)  # type: py.path.LocalPath
    res_path.copy(src_path)
    dst_path = py.path.local(src_path.dirname).join(src_path.purebasename + ".xml")
    opc_to_flat_opc(str(src_path), str(dst_path))
