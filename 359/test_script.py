import pytest
from typer.testing import CliRunner

from script import app

@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()

@pytest.mark.parametrize("a,b, c", (
        (2,1,1),
        (2,2,0),
        (2,4,-2),
        (0,0,0),
#        (-2,-2,0) DOES NOT WORK WITH ARGUMENTS NUMBERS
))
def test_app_subtract(runner, a, b, c):
    result = runner.invoke(app, ["subtract", f"{a}", f"{b}"])
    assert result.exit_code == 0
    assert result.stdout == f"The delta is {c}\n"

@pytest.mark.parametrize("c,d, evaluation", (
        (2,1,"not greater"),
        (2,2,"not greater"),
        (2,4,"greater"),
))
def test_app_compare(runner, c, d, evaluation):
    format = "d={} is {} than c={}\n"
    result = runner.invoke(app, ["compare", f"{c}", f"{d}"])
    assert result.exit_code == 0
    assert result.stdout == format.format(d,evaluation,c)

def test_app_help_compare(runner):
    result = runner.invoke(app, ["compare", "--help"])
    assert result.exit_code == 0
    assert "Command that checks whether a number d is greater than a number c" in result.output
    assert "First number to compare against" in result.output
    assert "Second number that is compared against first number" in result.output

def test_app_help_subtract(runner):
    result = runner.invoke(app, ["subtract", "--help"])
    assert result.exit_code == 0
    assert "Command that allows you to add two numbers." in result.output
    assert "The value of the first summand" in result.output
    assert "The value of the second summand" in result.output


@pytest.mark.parametrize("args", ([], ["1"]),)
@pytest.mark.parametrize("command", ("subtract", "compare"),)
def test_app_missing_args(runner,command, args):
    result = runner.invoke(app, [command]+args)
    assert result.exit_code == 2
    assert "Missing argument" in result.output