from morse.alphabet import ALPHABET, ALPHABET_REVERSED
from morse.exceptions import AlphabetValidationError, CodeCharactersValidationError


class Morse:
    def __init__(
        self,
        dot: str = ".",
        dash: str = "-",
    ) -> None:
        self.dot = dot
        self.dash = dash
        self.space = " "
        self._validate_encoding_chars()

    def encode(self, text: str) -> str:
        string_uppercase = text.upper()
        encoded = self._encode_without_translation(text=string_uppercase)
        return self._translate(code=encoded)

    def decode(self, code: str) -> str:
        self._validate_encoded_chars(code=code)
        return self._decode(code=code)

    def _encode_without_translation(self, text: str) -> str:
        self._validate_text_to_encode(text=text)
        morse_code = ""
        for character in text:
            morse_code += ALPHABET[character]
            morse_code += self.space
        return morse_code[0:-1]

    def _translate(self, code: str) -> str:
        translation_mapping = {".": self.dot, "-": self.dash}
        translation_table = str.maketrans(translation_mapping)
        return code.translate(translation_table)

    def _validate_encoding_chars(self) -> None:
        if self.dash == self.dot:
            raise CodeCharactersValidationError(
                "Characters for dot and dash must be different",
            )

    @staticmethod
    def _validate_text_to_encode(text: str) -> None:
        allowed_chars = set(ALPHABET.keys())
        text_chars = set(text)
        if text_chars.issubset(allowed_chars):
            return
        raise AlphabetValidationError(
            "String can only contain alphanumeric characters and spaces",
        )

    def _validate_encoded_chars(self, code: str) -> None:
        allowed_chars = {self.dot, self.dash, self.space}
        code_chars = set(code)
        if code_chars.issubset(allowed_chars):
            return
        raise CodeCharactersValidationError(
            f"Characters used in morse encoded string must be a subset of {code_chars}",
        )

    @staticmethod
    def _decode(code: str) -> str:
        code_split = code.split(" ")
        decoded_text = ""
        for encoded_letter in code_split:
            decoded_text += ALPHABET_REVERSED[encoded_letter]
        return decoded_text
