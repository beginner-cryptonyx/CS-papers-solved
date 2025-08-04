def IterativeCalculate(Number: int) -> int:
    Total: int = 0
    ToFind: int = Number
    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        Number = Number - 1
    return Total


print(IterativeCalculate(10))


# Better Implementation (cuz m bored)
# def BetterIterativeCalculate(Number: int) -> int:
#     total = 0
#     for i in range(1, Number + 1):
#         if Number % i == 0:
#             total += i
#     return total


# print(BetterIterativeCalculate(10))


# Recursive Approach
def RecursiveValue(Number: int, ToFind: int) -> int:
    if Number == 0:
        return 0
    else:
        if ToFind % Number == 0:
            return Number + RecursiveValue(Number - 1, ToFind)
        else:
            return RecursiveValue(Number - 1, ToFind)


print(RecursiveValue(50, 50))
