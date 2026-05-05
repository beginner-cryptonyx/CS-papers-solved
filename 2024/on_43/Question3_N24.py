"""
CORRECTIONS

OVERALL ---- 19/19

a - 2/2
b - 6/6
c - 2/2
    1/1
    1/1
d - 5/5
    1/1
    1/1
"""


# a 
global LinkedList, FirstEmpty, FirstNode
LinkedList:list[list[int]] = [[-1,i+1] for i in range(19)]
LinkedList.append([-1, -1])
FirstEmpty:int = 0
FirstNode:int = -1

# debug
def debug():
    for i, list in enumerate(LinkedList):
        print(i, list)
    print("FirstNode: ", FirstNode)
    print("FirstEmpty: ", FirstEmpty)
    

# b
def InsertData():
    global LinkedList, FirstEmpty, FirstNode
    for i in range(5):
        target = int(input("Enter the number that you want to insert into the linked list: "))
        if FirstEmpty == -1:
            break
        else:
            LinkedList[FirstEmpty][0] = target
            NextEmpty = LinkedList[FirstEmpty][1]
            LinkedList[FirstEmpty][1] = FirstNode
            
            FirstNode = FirstEmpty
            FirstEmpty = NextEmpty


# c i 
def OutputLinkedList():
    global LinkedList, FirstNode, FirstEmpty
    current_node = FirstNode
    while current_node != -1:
        print(LinkedList[current_node][0])
        current_node = LinkedList[current_node][1]

# c ii

InsertData()
OutputLinkedList()

# c iii
"""
Enter the number that you want to insert into the linked list: 5
Enter the number that you want to insert into the linked list: 1
Enter the number that you want to insert into the linked list: 2
Enter the number that you want to insert into the linked list: 3
Enter the number that you want to insert into the linked list: 8
8
3
2
1
5
"""

# d  i

def RemoveData(target:int):
    global LinkedList, FirstEmpty, FirstNode
    current_node:int = FirstNode
    old_node:int = FirstEmpty
    stop = False
    while current_node != -1 and not stop:
        if LinkedList[current_node][0] == target:
            stop = True
            if current_node == FirstNode:
                OldFirstNode = FirstNode
                FirstNode = LinkedList[FirstNode][1]
                LinkedList[OldFirstNode][1] = FirstEmpty
                FirstEmpty = OldFirstNode
            else:
                LinkedList[old_node][1] = LinkedList[current_node][1]
                LinkedList[current_node][1] = FirstEmpty
                FirstEmpty = current_node
        old_node = current_node
        current_node = LinkedList[current_node][1]

# d ii
RemoveData(5)
print('After')
# debug()
OutputLinkedList()

# d iii

"""
Enter the number that you want to insert into the linked list: 5
Enter the number that you want to insert into the linked list: 6
Enter the number that you want to insert into the linked list: 8
Enter the number that you want to insert into the linked list: 9
Enter the number that you want to insert into the linked list: 5
5
9
8
6
5
After
9
8
6
5



Enter the number that you want to insert into the linked list: 10 
Enter the number that you want to insert into the linked list: 7
Enter the number that you want to insert into the linked list: 8
Enter the number that you want to insert into the linked list: 5
Enter the number that you want to insert into the linked list: 6
6
5
8
7
10
After
6
8
7
10
"""