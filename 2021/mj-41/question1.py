# question a
class node():
    def __init__(self, data, next_node) -> None:
        self.data = data
        self.next_node = next_node


# question b
linkedList:list[node] = [
    node(1,1),
    node(5,4),
    node(6,7),
    node(7,-1),
    node(2,2),
    node(0,6),
    node(0,8),
    node(56,3),
    node(0,9),
    node(0,-1),
]

startPointer = 0
emptyList = 5

# question c i
def outputNodes(array:list[node], start_pointer:int) -> None:
    current_pointer = start_pointer
    if current_pointer != -1:
        print(array[current_pointer].data)
        outputNodes(array=array, start_pointer=array[current_pointer].next_node)

# c ii
outputNodes(linkedList, startPointer)


# d i
def addNode(array:list[node], start_pointer:int, empty_list_pointer:int) -> bool:
    value = int(input("What value to add to the linked list: "))
    
    # Free node operations
    if empty_list_pointer == -1:
        return False # no free list
    else:
        array[empty_list_pointer].data = value
        target_node = empty_list_pointer
        empty_list_pointer = array[empty_list_pointer].next_node
    
    # insertion
    if start_pointer == -1:
        return False # empty list
    current_node = start_pointer
    prev_node = -1
    while current_node != -1:
        prev_node = current_node
        current_node = array[current_node].next_node
    
    array[prev_node].next_node = target_node
    array[target_node].next_node = -1
    return True


# d ii
result = addNode(linkedList, startPointer, emptyList)
if addNode:
    print("Element added successfully")
else:
    print("Element could not be added")
    
    
outputNodes(linkedList, startPointer)