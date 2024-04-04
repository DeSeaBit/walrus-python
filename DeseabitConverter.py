from MorseConverter import *
from MorseBinaryConverter import *


class DeseabitEncoder:
    @staticmethod
    def encode(string: str) -> [int]:
        return MorseBinaryEncoder.encode(MorseEncoder.encode(string))


class DeseabitDecoder:
    @staticmethod
    def decode(binaries: [int]) -> str:
        return MorseDecoder.decode(MorseBinaryDecoder.decode(binaries))



x = DeseabitEncoder.encode("Bonjour comment vas-tu ?")
print(x)
print(DeseabitDecoder.decode(x))
