"""
CORRECTIONS

OVERALL ---- 27/27


a - 2/2
b - 5/5
c - 2/2
    2/2
d - 4/4
    1/1
e - 6/6
    3/3
    2/2

"""


# a
global DataStored, NumberItems
DataStored:list[int] = [] # Array of 20 integers
NumberItems:int # Integer

# b
def Initialise():
    global DataStored, NumberItems
    NumberItems = int(input("Quantity of numbers to add: "))
    while NumberItems > 20 or NumberItems < 1:
        NumberItems = int(input("Enter a valid quantity of numbers to add (between 1 and 20 only): "))
    for _ in range(NumberItems):
        item = int(input("Enter a number to add: "))
        DataStored.append(item)
        
# c
NumberItems = 0
Initialise()
print(DataStored)


# d i
def BubbleSort():
    global DataStored, NumberItems
    for i in range(NumberItems - 1):
        for j in range(NumberItems - i - 1):
            if DataStored[j] > DataStored[j+1]:
                temp = DataStored[j]
                DataStored[j] = DataStored[j+1]
                DataStored[j+1] = temp
# d ii                
BubbleSort()
print(DataStored)

# e i
def BinarySearch(DataToFind:int) -> int:
    global DataStored, NumberItems
    upper = NumberItems - 1
    lower = 0
    while upper >= lower:
        mid = (upper + lower) // 2
        if DataToFind == DataStored[mid]:
            return mid

        if DataToFind > DataStored[mid]:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1



# e ii

target = input("Enter a number to search: ")
res = BinarySearch(int(target))
print(res)
