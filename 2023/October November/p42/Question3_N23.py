# Whole code is wrong because I did not know about private attributes in python (using dunder "__")

import datetime

class Character():
    def __init__(self, CharacterName:str, DateOfBirth, Intelligence:float, Speed:int) -> None:
        # DECLARE CharacterName : STRING
        # DECLARE DateOfBirth : DATE
        # DECLARE Intelligence, Speed: INTEGER
        self.CharacterName = CharacterName
        self.DateOfBirth = DateOfBirth
        self.Intelligence = Intelligence
        self.Speed = Speed
    def GetIntelligence(self):
        return self.Intelligence
    def GetName(self):
        return self.CharacterName
    def SetIntelligence(self, intellect):
        self.Intelligence = intellect
    def Learn(self):
        self.Intelligence *= 1.1
    def ReturnAge(self):
        return 2023 - self.DateOfBirth.year

class MagicCharacter(Character):
    def __init__(self, CharacterName:str, DateOfBirth, Intelligence:float, Speed:int, Element:str):
        super().__init__(CharacterName, DateOfBirth, Intelligence, Speed)
        self.Element = Element
        
    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
            self.Intelligence *= 1.2
        elif self.Element =="earth":
            self.Intelligence *= 1.3
        else: 
            self.Intelligence *= 1.1

    
FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)
FirstCharacter.Learn()
print(FirstCharacter.GetName(), FirstCharacter.ReturnAge(),FirstCharacter.GetIntelligence())

FirstMagic = MagicCharacter("Light", DateOfBirth=datetime.datetime(2018, 3, 3), Intelligence=75, Speed=22, Element="fire")
FirstMagic.Learn()
print(FirstMagic.GetName(), FirstMagic.ReturnAge(),FirstMagic.GetIntelligence())
