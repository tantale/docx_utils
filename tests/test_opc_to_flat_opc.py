# coding: utf-8

from __future__ import absolute_import

import shutil

import pytest
from tests import PROJECT_DIR

from docx_utils.flatten import opc_to_flat_opc

try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib


@pytest.mark.parametrize(
    "relpath",
    [
        "tests/resources/test_opc_to_flat_opc/01-sterdyniak.docx",
        "tests/resources/test_opc_to_flat_opc/104_CODAP_1_2015_GA4.docx",
        "tests/resources/test_opc_to_flat_opc/MG40-MathGuide.docx",
        "tests/resources/test_opc_to_flat_opc/Mcycle_calculs_cherchons_ok.docx",
        "tests/resources/test_opc_to_flat_opc/Sample document with table.docx",
        "tests/resources/test_opc_to_flat_opc/Seminaire_DEA.docx",
        "tests/resources/test_opc_to_flat_opc/test-MsEq+MT.docx",
    ],
)
def test_opc_to_flat_opc(relpath, tmp_path):
    # type: (str, pathlib.Path) -> None
    res_path = pathlib.Path(PROJECT_DIR).joinpath(relpath)
    src_path = tmp_path.joinpath(res_path.name)
    shutil.copy2(str(res_path), str(src_path))
    dst_path = src_path.with_suffix(".xml")
    opc_to_flat_opc(str(src_path), str(dst_path), on_error="ignore")
