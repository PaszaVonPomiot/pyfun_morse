import logging

from morse.coders import Morse

logging.basicConfig(level=logging.INFO, format="%(message)s")


def main() -> None:
    morse = Morse()
    morse_encoded = morse.encode(text="ALA MA KOTA A KOT MA AIDS")
    logging.info(morse_encoded)
    morse_decoded = morse.decode(
        code=".- .-.. .-  -- .-  -.- --- - .-  .-  -.- --- -  -- .-  .- .. -.. ...",
    )
    logging.info(morse_decoded)


if __name__ == "__main__":
    main()
