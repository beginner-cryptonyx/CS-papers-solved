# a
class Card:
    def __init__(self, Number:int, Colour:str) -> None:
        self.__Number = Number # INTEGER
        self.__Colour = Colour # STRING
        
    # b
    def GetColour(self):
        return self.__Colour

    def GetNumber(self):
        return self.__Number    
    
    
# c
CardArray:list[Card] = []
try: 
    file = open("2022/mj_42/CardValues.txt", 'r')
    while file:
        number = file.readline().strip()
        color = file.readline().strip()
        if number == "" or color == "":
            break
        CardArray.append(Card(int(number), color))
    file.close()
except FileNotFoundError or IOError as e:
    print(f"Exception - unable to access file: {e}")
    
    
# d
ChosenCards = []
def ChooseCard():
    selection_number = -1 
    loop = True
    while selection_number < 0 or selection_number > 29 or loop:
        selection_number = int(input('enter number to choose the card: '))
        if CardArray[selection_number] in ChosenCards:
            print("Sorry, card has already been chosen")
        else:
            ChosenCards.append(CardArray[selection_number])
            loop = False
    return selection_number
    
# print([(card.GetColour(),card.GetNumber()) for card in CardArray]) 
# e
Player1:list[Card] = []
for _ in range(4):
    Player1.append(CardArray[ChooseCard()])
ChosenCards = []
for card in Player1:
    print(f"Number: {card.GetNumber()}\nColor: {card.GetColour()}")