import sys

import typer


def sum_numbers(a: int, b: int):
    return a + b


app = typer.Typer()
app.state = {"verbose": False}
state = app.state # To comply with the tests.


@app.command()
def sum(
        ctx: typer.Context,
        a: int = typer.Argument(..., help="The value of the first summand"),
        b: int = typer.Argument(..., help="The value of the second summand"),
):
    """Command that allows you to add two numbers."""
    sum_ab = sum_numbers(a, b)
    print(f"{'The sum is ' if app.state['verbose'] else ''}{sum_ab}")


@app.command()
def compare(
        ctx: typer.Context,
        c: int = typer.Argument(..., help="First number to compare against."),
        d: int = typer.Argument(..., help="Second number that is compared against first number."
    ),
):
    """Command that checks whether a number d is greater than a number c."""

    STRING_TRUE = "greater"
    STRING_FALSE = "not greater"

    d_greater_c = d > c

    c_evaluation = STRING_TRUE if d_greater_c else STRING_FALSE

    if app.state['verbose']:
        print(f"{d=} is {c_evaluation} than {c=}")
    else:
        print(f"d > c: {d_greater_c}")


@app.callback()
def main(
        ctx: typer.Context,
        verbose: bool = typer.Option(default=False, help=""),
):
    """
    Have sum fun with numbers.
    """
    app.state['verbose'] = verbose
    if verbose:
        print("Will write verbose output")



if __name__ == "__main__":
    app()