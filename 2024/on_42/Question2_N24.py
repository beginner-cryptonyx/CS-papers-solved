"""
CORRECTIONS

OVERALL ---- 26 / 29

a - 3/3
b - 3/3
c - 5/5
d - 3/3
e - 5/5
    1/2
f - 3/4
g - 3/3
    0/1
"""


# a
class Queue:
    def __init__(self, QueueArray:list[int], HeadPointer:int, TailPointer:int) -> None:
        self.QueueArray:list[int] = QueueArray # Array, 100 spaces for Integer
        self.HeadPointer:int = HeadPointer
        self.TailPointer:int = TailPointer
        
        
# b
TheQueue = Queue([-1 for _ in range(100)], -1 , 0)

# c

def Enqueue(AQueue:Queue, TheData:int):
    if AQueue.HeadPointer == -1:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.HeadPointer = 0
        AQueue.TailPointer = AQueue.TailPointer + 1
        return 1, AQueue
    elif AQueue.TailPointer > 99:
        return -1, AQueue
    else:
        AQueue.QueueArray[AQueue.TailPointer] = TheData
        AQueue.TailPointer = AQueue.TailPointer + 1
        return 1, AQueue
    
    
    
# d
def ReturnAllData():
    global TheQueue
    return_string = ""
    for i in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        return_string = f"{return_string} {str(TheQueue.QueueArray[i])}"
    return return_string

# e i 
for _ in range(10):
    number = int(input("Enter a number greater than or equal to 0 to add to the queue: "))
    while number < 0:
        number = int(input("Invalid Number entered. Enter a number greater than or equal to 0 to add to the queue: "))
    result, TheQueue = Enqueue(TheQueue, number)
    if result == -1:
        print('Queue is full')
    else:
        print(f"{number} was successfully added to the queue")

ReturnAllData() # I should have added print statement


# f
def Dequeue():
    global TheQueue
    if TheQueue.HeadPointer == -1: # more conditions hp = 100 or hp = tp
        return -1
    else:
        item = TheQueue.QueueArray[TheQueue.HeadPointer]
        TheQueue.HeadPointer = TheQueue.HeadPointer + 1
        return item    

# g i 
for _ in range(2):
    res = Dequeue()
    if res == -1:
        print("Queue empty")
    else:
        print(res)
        
ReturnAllData()