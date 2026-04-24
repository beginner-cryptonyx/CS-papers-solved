# a
from random import randint

ArrayData = [[randint(1,100) for _ in range(10)] for _ in range(10)] # 2D array of integer


# b  ii
def Output():
    for row in ArrayData:
        for column in row:
            print(column, end=" ")
        print("")
        
        

# b ii (second part)
print("Before Sorting")
Output()

# b i 
ArrayLength = 10 

for X in range(0, ArrayLength):
    for Y in range(0, ArrayLength - 1):
        for Z in range(0, ArrayLength - Y - 1):
            if ArrayData[X][Z] > ArrayData[X][Z+1]:
                TempValue = ArrayData[X][Z]
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempValue

# b ii (second part)
print('After Sorting')
Output()
                




# c  i 
def BinarySearch(SearchArray:list[list[int]], Lower, Upper, SearchValue) -> int:
    if Upper >= Lower:
        Mid = (Lower + Upper) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1 , Upper, SearchValue)
            
    return -1



# c ii
print(BinarySearch(ArrayData, 0, ArrayLength-1, int(input('Enter number to search for in the first line of the array: '))))

print(BinarySearch(ArrayData, 0, ArrayLength-1, int(input('Enter number to search for in the first line of the array: '))))