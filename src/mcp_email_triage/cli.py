"""Console script for mcp_email_triage."""

import typer
from rich.console import Console

from mcp_email_triage import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for mcp_email_triage."""
    console.print("Replace this message by putting your code into "
               "mcp_email_triage.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
