"""
CORRECTIONS

OVERALL ---- 31/31


a - 4/4 - But make sure to say its private too
b - 3/3
c - 2/2
d - 7/7 - But made proper mistakes > need to put in READ mode and need to CLOSE file
e - 5/5 - Though my initial thought for 
f - 7/7
g - 2/2
    1/1
"""



# a

class Character:
    # Name as String
    # XCoordinate as Integer
    # YCoordinate as Integer
    def __init__(self, Name:str, XCoordinate:int, YCoordinate:int) -> None:
        self.__Name:str = Name # String
        self.__XCoordinate:int = XCoordinate # Integer
        self.__YCoordinate:int = YCoordinate # Integer 
        
    #b
    def GetName(self) -> str:
        return self.__Name
    def GetX(self) -> int:
        return self.__XCoordinate
    def GetY(self) -> int:
        return self.__YCoordinate
    
    # c
    def ChangePosition(self, XChange:int, YChange:int):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange
        
        
        
# d 
CharacterArray:list[Character] = [] # List of 10 Characters
try:
    file = open("2022/on_42/Characters.txt")
    while file:
        name = file.readline().strip()
        if name == "":
            break
        x = file.readline().strip()
        y = file.readline().strip()
        CharacterArray.append(Character(name, int(x), int(y)))
except IOError or FileNotFoundError:
    print("File not Found")
    
# e

name = ""
index = -1
stop = False
while name not in map(lambda x: x.GetName(), CharacterArray):
    name = input("Enter the Name: ")
for i in range(len(CharacterArray)):
    if name == CharacterArray[i].GetName():
        index = i

# f

direction = input("Enter Direction your chosen character should move (W,A,S,D): ")
while direction not in ["W", "A", "S", "D"]:
    direction = input("Choose a correct direction from W,A,,D")
if direction == "W":
    CharacterArray[index].ChangePosition(0,1)
elif direction == "S":
    CharacterArray[index].ChangePosition(0,-1)
elif direction == "A":
    CharacterArray[index].ChangePosition(-1,0)
elif direction == "D":
    CharacterArray[index].ChangePosition(1,0)
    
    

print(f"{CharacterArray[index].GetName()} has changed coordinates to X = {CharacterArray[index].GetX()} and Y = {CharacterArray[index].GetY()}")