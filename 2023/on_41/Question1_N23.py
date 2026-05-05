# a i
def IterativeVowels(Value: str) -> int:
    Total: int
    LengthString: int
    FirstCharacter: str
    Total = 0
    LengthString = len(Value)
    for x in range(0, LengthString):
        FirstCharacter = Value[0]
        if (
            FirstCharacter == "a"
            or FirstCharacter == "e"
            or FirstCharacter == "i"
            or FirstCharacter == "o"
            or FirstCharacter == "u"
        ):
            Total += 1
        Value = Value[1 : len(Value)]
    return Total


# a ii
print(IterativeVowels("house"))

# a iii
"""
3
"""


# b i
def RecursiveVowels(Value: str):
    if len(Value) == 0:
        return 0
    else:
        if Value[0] in ["a", "e", "i", "o", "u"]:
            return RecursiveVowels(Value[1:]) + 1
        else:
            return RecursiveVowels(Value[1:])

# b ii

print(RecursiveVowels("imagine"))


# b iii

"""
3
4
"""
