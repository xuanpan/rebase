# src/rebase_cli/__init__.py

"""
Entry point for the Rebase CLI.

Rebase CLI - Legacy System Modernization Framework
Inspired by spec-kit, optimized for brownfield code modernization.
"""

import typer
from .commands.init import app as init_app

# Main CLI application
app = typer.Typer(
    name="rebase",
    help="Legacy System Modernization Framework - Transform legacy codebases with AI-driven workflows",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)

# Add commands
app.add_typer(init_app, name="init", help="Initialize modernization project")

def main():
    """Main entry point for the rebase CLI."""
    app()

if __name__ == "__main__":
    main()
