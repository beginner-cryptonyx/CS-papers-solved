"""
CORRECTIONS

OVERALL ---- 31/31

a - 4/4
    3/3
b - 7/7
c - 4/4
d - 2/2
    1/1
e - 6/6
    2/2
    2/2
"""


# a i 
class Tree:
    # private TreeName as string
    # private HeightGrowth as integer
    # private MaxHeight as integer
    # private MaxWidth as integer
    # private Evergreen as sting
    
    def __init__(self, TreeName, HeightGrowth:int, MaxHeight:int, MaxWidth:int, Evergreen:str) -> None:
        
        self.__TreeName:str = TreeName
        self.__HeightGrowth:int = HeightGrowth
        self.__MaxHeight:int = MaxHeight
        self.__MaxWidth:int = MaxWidth
        self.__Evergreen:str = Evergreen
    
    # a ii
    def GetTreeName(self):
        return self.__TreeName
    def GetGrowth(self):
        return self.__HeightGrowth
    def GetMaxHeight(self):
        return self.__MaxHeight
    def GetMaxWidth(self):
        return self.__MaxWidth
    def GetEvergreen(self):
        return self.__Evergreen

# b
def ReadData():
    TreeArray:list[Tree] = []


    try:
        file = open("2024/mj_41/Trees.txt")
        while True:
            line = file.readline().strip()
            if line == "":
                break
            line = line.split(",")
            TreeArray.append(Tree(line[0], int(line[1]), int(line[2]), int(line[3]), line[4]))
        
        # close the damn file
    except IOError:
        print("file not found")
        
    return TreeArray

# c
def PrintTrees(Tree:Tree):
    if Tree.GetEvergreen().lower() == "Yes":
        print(f"{Tree.GetTreeName()} has a maximum height {Tree.GetMaxHeight()} a maximum width {Tree.GetMaxWidth()} and grows {Tree.GetGrowth()} cm a year. It does not lose its leaves")
    else:
        print(f"{Tree.GetTreeName()} has a maximum height {Tree.GetMaxHeight()} a maximum width {Tree.GetMaxWidth()} and grows {Tree.GetGrowth()} cm a year. It loses its leaves each year")

# d i

TreeArray = ReadData()
PrintTrees(TreeArray[0])

# e 

def ChooseTrees(array:list[Tree]):
    max_height = int(input("Enter the max height of the tree (cm) : "))
    max_width = int(input("Enter the max width of the tree (cm): "))
    evergreen = ""
    while evergreen.lower() not in ["yes", "no"]:
        evergreen = input("Should the tree be evergreen? (Yes/No): ").lower()
    NewTreeList:list[Tree] = []
    for tree in array:
        if tree.GetEvergreen().lower() == evergreen and tree.GetMaxHeight() <= max_height and tree.GetMaxWidth() <= max_width:
            NewTreeList.append(tree)
    if len(NewTreeList) == 0:
        print("No trees with the selection entered was found")
    else:
        for tree in NewTreeList:
            PrintTrees(tree)
        tree_target = input("Enter the name of the tree you are wiling to buy: ").lower()
        target_found = False
        target_index = -1
        while not target_found:
            # Check if user has entered a tree name that is actually in their selection
            for i in range(len(NewTreeList)):
                if NewTreeList[i].GetTreeName().lower() == tree_target:
                    target_found = True
                    target_index = i
                    break
            if not target_found:
                tree_target = input("Enter the name of the tree you are wiling to buy: ").lower()
        starting_height  = int(input("What is the height of the tree when you initially bought it?: "))
        growth_rate = NewTreeList[target_index].GetGrowth()
        maximum_height = NewTreeList[target_index].GetMaxHeight()
        time = (maximum_height - starting_height)/growth_rate
        print(f"The tree will take {time} years to reach its maximum height of {maximum_height} cm")
        
        
ChooseTrees(TreeArray)