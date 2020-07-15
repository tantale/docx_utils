# coding: utf-8
import shutil

import pytest
from click.testing import CliRunner
from tests import PROJECT_DIR

import docx_utils
from docx_utils.cli import main


def test_main__version():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert result.output.strip() == "main, version {0}".format(docx_utils.__version__)


@pytest.mark.parametrize(
    "relpath",
    [
        "tests/resources/test_opc_to_flat_opc/Sample document with table.docx",
        "tests/resources/test_opc_to_flat_opc/cycle_calculs_cherchons_fail.docx",
    ],
)
def test_main__flatten(relpath, tmp_path):
    res_path = PROJECT_DIR.joinpath(relpath)
    src_path = tmp_path.joinpath(res_path.name)
    shutil.copy2(str(res_path), str(src_path))
    dst_path = src_path.with_suffix(".xml")
    runner = CliRunner()
    result = runner.invoke(main, ["flatten", str(src_path), str(dst_path)])
    assert result.exit_code == 0
    assert str(src_path) in result.output
    assert str(dst_path) in result.output


@pytest.mark.parametrize(
    "relpath",
    ["tests/resources/test_opc_to_flat_opc/cycle_calculs_cherchons_fail.docx",],
)
def test_main__flatten_fail(relpath, tmp_path):
    res_path = PROJECT_DIR.joinpath(relpath)
    src_path = tmp_path.joinpath(res_path.name)
    shutil.copy2(str(res_path), str(src_path))
    dst_path = src_path.with_suffix(".xml")
    runner = CliRunner()
    result = runner.invoke(
        main, ["flatten", str(src_path), str(dst_path), "--on-error", "strict"]
    )
    assert result.exit_code == 1
