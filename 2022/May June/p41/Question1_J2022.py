player_data = [["", ""] for _ in range(11)]

def ReadHighScores():
    try:
        with open("2022/May June/p41/HighScore.txt", "r") as file:
            content = file.read()
            content = content.split("\n")
            players = []
            scores = []
            for i in range(len(content)):
                if i % 2 == 0:
                    players.append(content[i])
                elif i % 2 == 1:
                    scores.append(content[i])
            for i in range(len(players)):
                player_data[i][0] = players[i]
                player_data[i][1] = scores[i]
    except FileNotFoundError as err:
        print(f"The file was not found. Traceback: {err}")

def OutputHighScores():
    for player, score in player_data:
        print(f"{player} {score}")
        
ReadHighScores()
OutputHighScores()

player_name = ""
int_score = -1

while len(player_name) != 3:
    player_name = input("Input a 3 character player name: ")

while int_score < 1 or int_score > 100000:
    int_score = int(input("Enter an integer score that is between 1 and 100,000 inclusive: "))