"""
CORRECTIONS 

OVERALL ---- 14 / 17

a - 2/2
b - 5/5
c - 2/2
d - 2/4
e - 2/2
    1/2

"""



# a
HighScores = [["", "", ""] for _ in range(7)] # 2 Dimensional Array of string

# b
def ReadData():
    array = []
    try:
        file = open("2024/on_42/HighScoreTable.txt", 'r')
        for i in range(7):
            id = file.readline().strip()
            game_level = file.readline().strip()
            score = file.readline().strip()
            array.append([id, game_level, score])
        file.close()
    except FileNotFoundError or IOError:
        print("File not found")
    finally:
        return array
        
# c
def OutputHighScores(array:list[list[str]]):
    for player_data in array:
        print(f"{player_data[0]} has reached level {player_data[1]} with a score of {player_data[2]}")
        
        
# q = ReadData()
# OutputHighScores(q)

# d
def SortScores(array:list[list[str]]):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j+1][1] > array[j][1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                
    return array

# print('----')
# OutputHighScores(SortScores(q))

# e i 


HighScores = ReadData()
print("Before")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After")
OutputHighScores(HighScores)