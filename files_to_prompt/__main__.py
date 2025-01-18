from .cli import cli

if __name__ == "__main__":
    print("Debug: Running from __main__.py", file=sys.stderr)
    cli()