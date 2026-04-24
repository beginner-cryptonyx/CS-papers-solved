# a
class Picture():
    def __init__(self, Description: str, Width:int, Height:int, FrameColour: str) -> None:
        # Description, FrameColour : String
        # Width, Height : Integer
        self.__Description = Description 
        self.__Width = Width
        self.__Height = Height
        self.__FrameColour = FrameColour
    
    
    # b
    def GetDescription(self) -> str:
        return self.__Description
    def GetHeight(self) -> int:
        return self.__Height
    def GetWidth(self) -> int:
        return self.__Width
    def GetFrameColour(self) -> str:
        return self.__FrameColour
    
    
    
    # c
    def SetDescription(self, NewDescription:str) -> None:
        self.__Description = NewDescription
    


# d
# PictureArray: Array[0:100] OF Picture
PictureArray:list[Picture] = [] # 100 elements
"""
post correction, since question asked the length to be 100 elements, we need to make sure there are 100 elements


PictureArray = []
for i in range(100):
    PictureArray.append(Picture("",0,0,"")) 
    
this is the correct solution
"""



# e
"""
post correction:
1. Array needs to be globalised
2. bad counting logic

"""
def ReadData():
    try:
        file = open("2021/on-42/Pictures.txt", 'r') #1
        counter = 0
        PictureAttributes = ["", 0, 0, ""]
        while True:
            line = file.readline().strip()
            if line == "":
                break # 2
            if counter == 1 or counter == 2:
                PictureAttributes[counter] = int(line)
            elif counter == 0 or counter == 3:
                PictureAttributes[counter] = line
            counter = counter + 1
            if counter == 4:
                counter = 0
                PictureArray.append(Picture(*PictureAttributes)) #3 #4
        file.close()
        return len(PictureArray) 
    except FileNotFoundError as e:
        print(f"File Not Found: {e}") 


# f      
ReadData()
# print(len(PictureArray))
# for item in PictureArray:
#     print(item.GetDescription(), item.GetWidth(), item.GetHeight(), item.GetFrameColour())

# g
"""
Corrections:
take 3 input - 1
covert color to lowercase - 1
loop through array - 1
use ReadData value as index - 0

check color match - 1
check width - 1
check hieght - 1
all using get method - 1

output desc width and height - 0
"""

color = input("Enter the colour of the frame: ")
max_width = int(input("Enter the maximum width of the frame: "))
max_height = int(input("Enter the maximum height of the frame: "))


for item in PictureArray:
    if item.GetFrameColour() == color.lower() and item.GetHeight() <= max_height and item.GetWidth() <= max_width:
        print(item.GetDescription())
