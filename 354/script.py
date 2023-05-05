import typer


def sum_numbers(a: int, b: int):
    return a + b


def main(
    a: int = typer.Argument(..., help="The value of the first summand"),
    b: int = typer.Argument(..., help="The value of the second summand"),
    c: int = typer.Option(None, help="")
):
    """CLI that allows you to add two numbers"""
    sum_ = sum_numbers(a, b)
    conditional_text_from_option_c = f"{' not' if c >= sum_ else ''} smaller" if c else " None"
    print(f"The sum is {sum_} and c is{conditional_text_from_option_c}")


if __name__ == "__main__":
    typer.run(main)