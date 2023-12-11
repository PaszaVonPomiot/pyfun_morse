import logging

from morse.coder import Morse

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main() -> None:
    morse = Morse()
    morse_encoded = morse.encode(string="Ala ma wszystko w dupie 69")
    logging.info(morse_encoded)


if __name__ == "__main__":
    main()
