"""
CORRECTIONS

OVERALL ---- 23/23

a - 2/2
b - 6/6
c - 7/7
d - 3/3
    1/1
e - 4/4

"""

# a
global DataArray
DataArray:list[int] = [0 for _ in range(100)] # list of 100 integers

# b
def ReadFile():
    global DataArray
    try:
        file = open("2022/on_41/IntegerData.txt", 'r')
        for i in range(100):
            line = file.readline().strip()
            DataArray[i] = int(line)
        file.close()
    except FileNotFoundError or IOError:
        print("Could not access the file")
        
# c
def FindValues():
    global DataArray
    number = 0
    while number < 1 or number > 100:
        number = int(input("What number do you want to look for?: "))
    count = 0
    for i in range(100):
        if DataArray[i] == number:
            count = count + 1
    return count

# d i 
ReadFile()
res = FindValues()
print(f"The number has been found {res} times")


# d ii
"""
What number do you want to look for?: 61
The number has been found 2 times
"""


# e
def BubbleSort():
    global DataArray
    for i in range(100 - 1):
        for j in range(100 - i - 1):
            if DataArray[j] > DataArray[j+1]:
                temp = DataArray[j]
                DataArray[j] = DataArray[j+1]
                DataArray[j+1] = temp
    print(DataArray)
    
    
BubbleSort()