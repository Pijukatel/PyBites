import typer

app = typer.Typer()


@app.command()
def main(
        username: str = typer.Argument(default=...),
        password: str = typer.Option(default =..., prompt=True, hide_input=True)
):
    print(f"Hello {username}. Doing something very secure with password.\n"
    f"...just kidding, here it is, very insecure: {password}\n")


if __name__ == "__main__":
    app()