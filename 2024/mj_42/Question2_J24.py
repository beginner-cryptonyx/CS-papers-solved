"""
CORRECTIONS

OVERALL ---- 27/30

a - 4/4
    3/3
    3/3
b - 3/4
    6/6
    3/4
c - 1/1
    4/4
    0/1
"""



# a i 
class Node():
    # private LeftPointer as Integer
    # private RightPointer as Integer
    # private Data as Integer
    def __init__(self, Pdata:int) -> None:
        self.__Data:int = Pdata # integer
        self.__LeftPointer:int = -1 # Integer
        self.__RightPointer:int = -1 # Integer
    
    # a ii
    def GetData(self) -> int:
        return self.__Data
    def GetRight(self) -> int:
        return self.__RightPointer
    def GetLeft(self) -> int:
        return self.__LeftPointer
    
    # a iii
    def SetData(self, value:int) -> None:
        self.__Data = value
    def SetLeft(self, value:int) -> None:
        self.__LeftPointer = value
    def SetRight(self, value:int) -> None:
        self.__RightPointer = value
        
# b i 
class TreeClass():
    # Tree as Array(20) of Node
    # FirstNode as Integer
    # NumberNodes as Integers
    def __init__(self) -> None:
        self.FirstNode:int = -1
        self.NumberNodes:int = 0
        self.Tree:list[Node] = [Node(-1) for _ in range(20)]
        
    # b ii

    def InsertNode(self, NewNode:Node) -> None:
        if self.NumberNodes == 0:
            self.Tree[self.NumberNodes] = NewNode
            self.NumberNodes += 1
            self.FirstNode = 0
        elif self.NumberNodes == 20:
            print("Tree is full")
        else:
            self.Tree[self.NumberNodes] = NewNode
            current_pointer = self.FirstNode
            stop = False
            while not stop:
                if self.Tree[current_pointer].GetData() < NewNode.GetData(): # target > curr node
                    # right
                    if self.Tree[current_pointer].GetRight() == -1:
                        self.Tree[current_pointer].SetRight(self.NumberNodes)
                        stop = True
                    current_pointer = self.Tree[current_pointer].GetRight()
                elif self.Tree[current_pointer].GetData() > NewNode.GetData(): # target < curr node
                    # left
                    if self.Tree[current_pointer].GetLeft() == -1:
                        self.Tree[current_pointer].SetLeft(self.NumberNodes)
                        stop = True
                    current_pointer = self.Tree[current_pointer].GetLeft()
            self.NumberNodes += 1
    
    # b iii
    def OutputTree(self):
        if self.FirstNode == -1:
            print("No Nodes")
        else:
            for node in self.Tree:
                print(node.GetLeft(), node.GetData(), node.GetRight())

# c i 
TheTree = TreeClass()


# c ii
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))

TheTree.OutputTree()

# c iii
"""
2 10 1
-1 11 4
3 5 5
-1 1 -1
6 20 -1
-1 7 -1
-1 15 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
-1 -1 -1
"""