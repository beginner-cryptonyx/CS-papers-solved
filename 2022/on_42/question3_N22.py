"""
CORRECTIONS

OVERALL ---- 20/21
 
a - 3/3
b - 6/6
c - 4/4
d - 5/6 - needed to make base case same as pseudocode which had `start == 0` as base
e - 1/1
    1/1

"""



# a
global Queue, HeadPointer, TailPointer
Queue = [0 for _ in range(100)] # array of 100 integer
HeadPointer = -1 # integer
TailPointer = 0 # integer

# b
def Enqueue(value:int) -> bool:
    global Queue, HeadPointer, TailPointer
    if TailPointer == 100:
        return False
    else:
        Queue[TailPointer] = value
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0
        return True

# c
output = "Successful"
for i in range(1,21):
    result = Enqueue(i)
    if result == False:
        output = "Unsuccessful"
print(output)

# d
# Start is probably tail pointer
def RecursiveOutput(start:int):
    global Queue, HeadPointer, TailPointer
    if start == -1:
        return 0
    else:
        return RecursiveOutput(start - 1) + Queue[start]

# e
print(RecursiveOutput(TailPointer))