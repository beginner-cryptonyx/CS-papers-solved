# a

"""
post correction - again question says 10 integers meaning there needs to be 10 INTEGERS
"""

global StackData, StackPointer
StackPointer = 0
StackData:list = [None for _ in range(10)] # 100 integers

# b
def OutputAll():
    global StackData, StackPointer
    for element in StackData:
        print(element)
    print("stack pointer:",StackPointer)
    
    
# c
def Push(target:int) -> bool:
    global StackData, StackPointer
    if StackPointer > 9:
        return False
    else:
        StackData[StackPointer] = target
        StackPointer = StackPointer + 1
        return True
    
# d i 
for _ in range(11):
    target = int(input("Enter a number to add to the stack: "))
    result = Push(target)
    if result is True:
        print(f"{target} has been added")
    else:
        print(f"{target} could not be added as stack is full")
OutputAll()


# e i
def Pop() -> int:
    global StackData, StackPointer
    if StackPointer == 0:
        return -1
    else:
        item = StackData[StackPointer-1]
        StackPointer = StackPointer - 1
        return item

# e ii
Pop()
Pop()
OutputAll()