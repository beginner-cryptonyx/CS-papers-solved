# a
global ArrayNodes
ArrayNodes:list[list[int]] = [[-1,-1,-1] for _ in range(20)]

# b

ArrayNodes[0] = [1, 20, 5]
ArrayNodes[1] = [2, 15, -1]
ArrayNodes[2] = [-1, 3, 3]
ArrayNodes[3] = [-1, 9, 4]
ArrayNodes[4] = [-1, 10, -1]
ArrayNodes[5] = [-1, 58, -1]
ArrayNodes[6] = [-1, -1, -1]

FreeNode:int = 6
RootPointer:int = 0

# c
def SearchValue(Root:int, ValueToFind:int):
    global ArrayNodes
    
    if Root == -1:
        return -1
    elif ArrayNodes[Root][1] == ValueToFind:
        return Root
    elif ArrayNodes[Root][1] == -1:
        return -1
    
    if ArrayNodes[Root][1] >  ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    
    
# d
def PostOrder(root:int):
    global ArrayNodes
    if root != -1 and ArrayNodes[root][1] != -1:
        if ArrayNodes[root][0] != -1:
            PostOrder(ArrayNodes[root][0])
        if ArrayNodes[root][2] != -1:
            PostOrder(ArrayNodes[root][2])
        print(ArrayNodes[root][1])

# e i 
res = SearchValue(RootPointer, 15)
print(f"15 is stored in index {res}")
PostOrder(RootPointer)

# e ii
"""
15 is stored in index 1
10
9
3
15
58
20
"""