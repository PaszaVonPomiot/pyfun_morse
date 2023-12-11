from morse.alphabet import CODE
from morse.exceptions import AlphabetValidationError, CodeCharactersValidationError


class Morse:
    def __init__(
        self,
        dot: str = "·",
        dash: str = "-",
    ) -> None:
        self.dot = dot
        self.dash = dash
        self._validate_code_chars()

    def encode(self, string: str) -> str:
        string_uppercase = string.upper()
        encoded = self._encode_without_translation(string=string_uppercase)
        return self._translate(encoded_str=encoded)

    def _encode_without_translation(self, string: str) -> str:
        self._validate_alphabet(string=string)
        morse_code = ""
        for character in string:
            morse_code += CODE[character]
            morse_code += " "
        return morse_code[0:-1]

    def _translate(self, encoded_str: str) -> str:
        translation_mapping = {"·": self.dot, "-": self.dash}
        translation_table = str.maketrans(translation_mapping)
        return encoded_str.translate(translation_table)

    def _validate_code_chars(self) -> None:
        if self.dash == self.dot:
            raise CodeCharactersValidationError(
                "Characters for dot and dash must be different",
            )

    @staticmethod
    def _validate_alphabet(string: str) -> None:
        alphabet_chars = set(CODE.keys())
        string_chars = set(string)
        if string_chars.issubset(alphabet_chars):
            return
        raise AlphabetValidationError(
            "String can only contain alphanumeric characters and spaces",
        )
