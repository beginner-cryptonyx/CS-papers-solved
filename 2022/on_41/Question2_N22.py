"""
CORRECTIONS

OVERALL ----


a - 4/4
    3/3
    2/2
b - 4/6
    2/2
    1/1
    
"""


# a i
class Card:
    # private number as integer
    # private colour as string
    def __init__(self, number:int, colour:str) -> None:
        self.__Number:int = number # integer between 1 and 5 inclusive
        self.__Colour:str = colour # string with values red, blue or yellow
        

        
    # a ii
    def GetNumber(self) -> int:
        return self.__Number
    def GetColour(self) -> str:
        return self.__Colour
    

# a iii
RedCard1 = Card(1, "red")
RedCard2 = Card(2, "red")
RedCard3 = Card(3, "red")
RedCard4 = Card(4, "red")
RedCard5 = Card(5, "red")

YellowCard1 = Card(1, "yellow")
YellowCard2 = Card(2, "yellow")
YellowCard3 = Card(3, "yellow")
YellowCard4 = Card(4, "yellow")
YellowCard5 = Card(5, "yellow")

BlueCard1 = Card(1, "blue")
BlueCard2 = Card(2, "blue")
BlueCard3 = Card(3, "blue")
BlueCard4 = Card(4, "blue")
BlueCard5 = Card(5, "blue")


# b i
class Hand:
    # private Cards as array(9) of card
    # private FirstCard as integer
    # private NumberCards as integer
    
    def __init__(self, Cards:list[Card]):
        self.__Cards:list[Card] = Cards # List of cards with 9 elements
        self.__FirstCards:int = 0 # integer
        self.__NumberCards:int = 5 # integer
        
    # b ii
    def GetCard(self, index:int) -> Card:
        return self.__Cards[index]
    
# b iii
Player1 = Hand([RedCard1, RedCard2, RedCard3, RedCard4, YellowCard1])
Player2 = Hand([YellowCard2, YellowCard3, YellowCard4, YellowCard5, BlueCard1])

# c i 
def CalculateValue(hand:Hand) -> int:
    points = 0
    for i in range(5):
        card = hand.GetCard(i)
        color = card.GetColour()
        
        if color == "red":
            points = points + 5
        elif color == "blue":
            points = points + 10
        elif color == "yellow":
            points = points + 15
        
        points = points + card.GetNumber()
    return points
        
# c ii
Player1Score = CalculateValue(Player1)
Player2Score = CalculateValue(Player2)

if Player1Score > Player2Score:
    print("Player 1 has won")
elif Player2Score > Player1Score:
    print("Player 2 has won")
else:
    print("Game is a draw")
    
    
# c iii
"""
Player 2 has won
"""
