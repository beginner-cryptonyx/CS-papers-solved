# a
# ArrayNodes: ARRAY[0:19 , 0:2] OF INTEGER
# RootPointer, FreeNode: INTEGER
ArrayNodes:list[list[int]] = [[-1,-1,-1] for _ in range(20)]
RootPointer:int = -1 
FreeNode:int = 0

# b
def AddNode(x):
    global FreeNode, RootPointer, ArrayNodes
    print('Enter the data')
    NodeData = x
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1 
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1 
        
        if RootPointer ==  -1:
            RootPointer = 0
        else:
            Placed:bool = False
            CurrentNode = RootPointer
            while not Placed :
                if NodeData <= ArrayNodes[CurrentNode][1]: #Post Correction - bad comparison, as each node is unique
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else: 
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode  + 1
    else:
        print('Tree is full')
    return ArrayNodes, RootPointer, FreeNode


# c
def PrintAll():
    for left, data, right in ArrayNodes:
        print(left, data, right)
            
# d i
# for _ in range(10):
#     ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

# PrintAll()

# e i 

            
### Going to try again with help of hints from Deepseek
for i in [10,5,15,8,12,6,20,11,9,4]:
    AddNode(i)
PrintAll()


"""
corrections

taking param for current node - 1
chceck left node empty - 1
    if not call recursively with left pointer as current - 1
output value - 1
check right node - 1
    if not empty recursive - 1
correct order - 1
    
"""

def InOrder(root):
    if ArrayNodes[root][0] != -1:
        InOrder(ArrayNodes[root][0])
    print(ArrayNodes[root][1])
    if ArrayNodes[root][2] != -1:
        InOrder(ArrayNodes[root][2])
    
         
InOrder(RootPointer)