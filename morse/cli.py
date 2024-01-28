import logging

import click
from coders import Morse

logging.basicConfig(level=logging.INFO, format="%(message)s")


@click.command()
@click.argument("text")
def cli(text: str) -> None:
    morse = Morse()
    encoded_text = morse.encode(text)
    logging.info(encoded_text)


if __name__ == "__main__":
    cli()
