player_data: list[list[str | int]] = [[None, None] for _ in range(11)]


def ReadHighScores():
    with open("HighScore.txt", "r") as f:
        content = f.read()
        content = content.split("\n")
        for index, item in enumerate(content):
            if index % 2 == 0:  # player name
                player_data[int(index / 2)][0] = item
            else:
                player_data[int((index - 1) / 2)][1] = item


def OutputHighScores():
    for player in player_data:
        print(player[0], player[1])


ReadHighScores()
OutputHighScores()
