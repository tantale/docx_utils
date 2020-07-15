# coding: utf-8

from __future__ import absolute_import

import shutil

import pytest
from tests import PROJECT_DIR

from docx_utils.emboss import flat_opc_to_office


@pytest.mark.parametrize(
    "relpath",
    [
        "tests/resources/test_flat_opc_to_office/01-sterdyniak.xml",
        "tests/resources/test_flat_opc_to_office/104_CODAP_1_2015_GA4.xml",
        "tests/resources/test_flat_opc_to_office/MG40-MathGuide.xml",
        "tests/resources/test_flat_opc_to_office/cycle_calculs_cherchons_fail.xml",
        "tests/resources/test_flat_opc_to_office/Sample document with table.xml",
        "tests/resources/test_flat_opc_to_office/Seminaire_DEA.xml",
        "tests/resources/test_flat_opc_to_office/test-MsEq+MT.xml",
    ],
)
def test_flat_opc_to_office(relpath, tmp_path):
    res_path = PROJECT_DIR.joinpath(relpath)
    src_path = tmp_path.joinpath(res_path.name)
    shutil.copy2(str(res_path), str(src_path))
    dst_path = src_path.with_suffix(".docx")
    flat_opc_to_office(str(src_path), str(dst_path))
