import pytest
from typer.testing import CliRunner

from script import app


@pytest.fixture()
def runner() -> CliRunner:
    return CliRunner()

def test_app_main_flow(runner):
    name = "SomeName"
    result = runner.invoke(app, [name])
    assert result.exit_code == 0
    assert result.output == f"Hello {name}!\n"

def test_app_help(runner):
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "CLI that allows you to greet a person." in result.output
    assert "The name of the person to greet." in result.output
