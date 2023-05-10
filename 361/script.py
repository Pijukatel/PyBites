import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(invoke_without_command=True)

@app.callback()
def main():
    table = Table("Name", "Favorite Tool/Framework")
    table.add_row("Bob", "Vim")
    table.add_row("Julian", "Flask")
    table.add_row("Robin", "VS Code")
    Console().print(table)


if __name__ == "__main__":
    app()