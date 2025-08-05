class Balloon:
    def __init__(self, defence_item, color):
        # DECLARE __health: INTEGER
        # DECLARE __defence_item: STRING
        # DECLARE __color: STRING
        self.__health = 100
        self.__defence_item = defence_item
        self.__color = color
        
    
    def GetDefenceItem(self):
        return self.__defence_item

    def ChangeHealth(self, change:int):
        self.__health += change
    
    def CheckHealth(self):
        if self.__health <= 0:
            return True
        else:
            return False

def Defend(balloon:Balloon):
    strength = input("Opponent Strength: ")
    balloon.ChangeHealth(-int(strength))
    print(balloon.GetDefenceItem())
    has_no_heath = balloon.CheckHealth()
    if not has_no_heath:
        print("Balloon still has health!")
    else:
        print("Balloon has no heath left :(")
    return balloon

defence_item = input("Enter defence item for balloon to use: ")
color = input("Enter color of the balloon: ")

Balloon1 = Balloon(defence_item, color)

Defend(Balloon1)