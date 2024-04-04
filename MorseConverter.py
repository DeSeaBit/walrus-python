import json

with open("extended_morse_table.json", "r") as f:
    morse_table = json.load(f)


class MorseEncoder:
    @staticmethod
    def encode(string: str) -> str:
        morse_code = []
        for char in string:
            if char.lower() in morse_table:
                if char.isupper():
                    morse_code.append(morse_table["MAJ"])
                morse_code.append(morse_table[char.lower()])
        return " ".join(morse_code)


class MorseDecoder:
    @staticmethod
    def decode(morse: str) -> str:
        morse_list = morse.split(" ")
        is_next_upper = False
        result = ""
        for morse in morse_list:
            for key, value in morse_table.items():
                if value == morse:
                    if key == "MAJ":
                        is_next_upper = True
                    elif is_next_upper:
                        result += key.upper()
                        is_next_upper = False
                    else:
                        result += key.lower()
                    break
        return result
