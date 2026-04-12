# a
arrayData:list[int] = [10,5,6,7,1,12,13,15,21,8]

# b i

def linearSearch(target:int) -> bool:
    for i in range(len(arrayData)):
        if arrayData[i] == target:
            return True
    return False


# b ii
value = int(input("Enter the value that should be searched: "))
result = linearSearch(value)
if result:
    print(f"{value} was found")
else:
    print(f"{value} was NOT found")
    

# c
def bubbleSort():
    temp:int
    for x in range(0, 9): 
        for y in range(0,9-x):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp
                