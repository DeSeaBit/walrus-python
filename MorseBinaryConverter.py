class MorseBinaryEncoder:
    @staticmethod
    def encode(morse: str) -> [int]:
        strings = morse.split(" ")
        binaries = []
        for string in strings:
            binary = ""
            for n in string:
                if n == ".":
                    binary += "10"
                elif n == "-":
                    binary += "11"
            binaries.append(int(binary, 2))
        return binaries


class MorseBinaryDecoder:
    @staticmethod
    def decode(binaries: [int]) -> str:
        decoded = ""
        for binary in binaries:
            string = format(binary, 'b')
            strings = [string[i:i + 2] for i in range(0, len(string), 2)]
            for n in strings:
                if n == "10":
                    decoded += "."
                elif n == "11":
                    decoded += "-"
            decoded += " "
        return decoded
