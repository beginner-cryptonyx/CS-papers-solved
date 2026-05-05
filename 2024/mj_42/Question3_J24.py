"""
CORRECTIONS

OVERALL ---- 22/23

a - 1/1
b - 4/4
    2/2
    1/1
c - 3/4
    1/1
    1/1
d - 6/6
    2/2
    1/1
"""


# a 
NumberArray = [100, 85, 644, 22, 15, 8 ,1]
# b
global LastItem, CheckItem, LoopAgain
LastItem:int
CheckItem:int
LoopAgain:bool

def RecursiveIteration(IntegerArray:list[int], NumberElements:int) -> list[int]:
    global LastItem, CheckItem, LoopAgain   

    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveIteration(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
        
    LoopAgain = True
    
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] <= LastItem:
        LoopAgain = False
    
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] <= LastItem:
            LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray


# b ii
NewNumberArray = RecursiveIteration(NumberArray, len(NumberArray))
print("recursive")
print(NewNumberArray)

# b iii
"""
recursive
[1, 8, 15, 22, 85, 100, 644]
"""

# c 
def IterativeInsertion(array:list[int]):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        
        while j>0 and array[j-1] >= key:
            array[j-1] = array[j]
            j -= 1
            
        array[j] = key
    return array


# c ii
iterative_sorted_array = IterativeInsertion(NumberArray)
print('iterative')
print(iterative_sorted_array)

# c iii
"""
recursive
[1, 8, 15, 22, 85, 100, 644]
iterative
[1, 8, 15, 22, 85, 100, 644]
"""


# d i 
def BinarySearch(IntegerArray:list[int], First:int, Last:int, ToFind:int) -> int:
    mid = (First + Last) // 2
    if IntegerArray[mid] == ToFind:
        return mid
    elif First > Last:
        return -1
    elif ToFind > IntegerArray[mid]:
        return BinarySearch(IntegerArray, mid + 1, Last, ToFind)
    else:
        return BinarySearch(IntegerArray, First, mid - 1, ToFind)

# d ii
res = BinarySearch(NumberArray, 0, 6, 644)

if res == -1:
    print("Not Found")
else:
    print(res)
    
    
    
# d iii
"""
recursive
[1, 8, 15, 22, 85, 100, 644]
iterative
[1, 8, 15, 22, 85, 100, 644]
6
"""