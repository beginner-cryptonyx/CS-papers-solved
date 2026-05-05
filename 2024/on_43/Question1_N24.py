"""
CORRECTIONS

OVERALL ---- 21/22

a - 5/6 (somehow missed exception handling and clos???) 
b - 2/2
    3/3
    1/1
c - 4/4
d - 3/3
    2/2
    1/1
    
"""


# a 
def ReadData() -> list[str]:
    string_array:list[str] = []
    file_name = "2024/on_43/Data.txt"
    file = open(file_name, 'r')
    for _ in range(45):
        line = file.readline().strip()
        string_array.append(line)
    return string_array

# b i
def FormatArray(array:list[str]) -> str:
    return_string = ""
    for string in array:
        return_string = f"{return_string} {string}"
    return return_string

# b ii 
array = ReadData()
string = FormatArray(array)
print(string)

# b iii
"""
beige green scarlet silver bronze slate yellow orange jade lavender magnolia magenta turquoise black grey russet maroon mango mint purple red pink white cream navy olive brown violet cyan amber aqua azure copper fawn fuschia gold indigo ivory mauve mulberry peach periwinkle plum rose sage
"""

# c

def CompareStrings(string_1:str, string_2:str) -> int:
    max_iterations = min(len(string_1), len(string_2))
    return_int = 0
    stop = False
    count = 0
    while not stop and count < max_iterations:
        if string_1[count] == string_2[count]:
            count += 1
        elif string_1[count] < string_2[count]:
            stop = True
            return_int = 1
        else:
            stop = True
            return_int = 2
    return return_int
      
        
# d i 
def Bubble(array:list[str]):
    length = len(array)
    
    for i in range(length - 1):
        for j in range(length - i - 1):
            if CompareStrings(array[j], array[j+1]) == 2: #swap
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


# d ii
sorted_array = Bubble(array)
sorted_formatted_array = FormatArray(sorted_array)
print(sorted_formatted_array)


# iii
"""
beige green scarlet silver bronze slate yellow orange jade lavender magnolia magenta turquoise black grey russet maroon mango mint purple red pink white cream navy olive brown violet cyan amber aqua azure copper fawn fuschia gold indigo ivory mauve mulberry peach periwinkle plum rose sage
amber aqua azure beige black bronze brown copper cream cyan fawn fuschia gold green grey indigo ivory jade lavender magenta magnolia mango maroon mauve mint mulberry navy olive orange peach periwinkle pink plum purple red rose russet sage scarlet silver slate turquoise violet white yellow
"""

