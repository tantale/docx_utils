# coding: utf-8
import py
from click.testing import CliRunner
from tests import PROJECT_DIR

import docx_utils
from docx_utils.cli import main


def test_main__version():
    runner = CliRunner()
    result = runner.invoke(main, ['--version'])
    assert result.exit_code == 0
    assert result.output.strip() == 'main, version {0}'.format(docx_utils.__version__)


def test_main_flatten(tmpdir):
    # type: (py.path.LocalPath) -> None
    relpath = 'tests/resources/test_opc_to_flat_opc/Sample document with table.docx'
    res_path = py.path.local(PROJECT_DIR).join(relpath)  # type: py.path.LocalPath
    src_path = tmpdir.join(res_path.basename)  # type: py.path.LocalPath
    res_path.copy(src_path)
    dst_path = py.path.local(src_path.dirname).join(src_path.purebasename + ".xml")
    runner = CliRunner()
    result = runner.invoke(main, ['flatten', str(src_path), str(dst_path)])
    assert result.exit_code == 0
    assert str(src_path) in result.output
    assert str(dst_path) in result.output
