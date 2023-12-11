from morse.alphabet import CODE
from morse.exceptions import AlphabetValidationError


class Morse:
    def __init__(
        self,
        dot: str = "·",
        dash: str = "-",
    ) -> None:
        self.dot = dot
        self.dash = dash
        self._validate_alphabet()

    def encode(self, string: str) -> str:
        encoded = self._encode_without_translation(string=string)
        return self._translate(encoded_str=encoded)

    @staticmethod
    def _encode_without_translation(string: str) -> str:
        morse_code = ""
        for character in string:
            morse_code += CODE[character]
            morse_code += " "
        return morse_code[0:-1]

    def _translate(self, encoded_str: str) -> str:
        translation_mapping = {".": self.dot, "-": self.dash}
        translation_table = str.maketrans(translation_mapping)
        return encoded_str.translate(translation_table)

    def _validate_alphabet(self) -> None:
        if self.dash == self.dot:
            raise AlphabetValidationError(
                "Characters for dot and dash must be different",
            )


if __name__ == "__main__":
    morse = Morse(dot="·")
    morse_encoded = morse.encode(string="DUPA 69")
