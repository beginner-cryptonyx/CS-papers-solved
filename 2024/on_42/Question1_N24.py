"""
CORRECTIONS

OVERALL ---- 29/29

a - 4/4
    3/3
b - 1/1
    3/3
c - 4/4
d - 4/4
e - 2/2
    7/7
    1/1
"""

# a i
class EventItem:
    # private EventName as String
    # private Type as String
    # private Difficulty as Integer
    def __init__(self, EventName:str, Type:str, Difficulty:int) -> None:
        self.__EventName:str = EventName
        self.__Type:str = Type
        self.__Difficulty:int = Difficulty
    
    # a ii
    def GetName(self):
        return self.__EventName
    def GetEventType(self):
        return self.__Type
    def GetDifficulty(self):
        return self.__Difficulty

# c
class Character:
    # private CharacterName as String
    # private Jump as Integer
    # private Swim as Integer
    # private Run as Integer
    # private Drive as Integer
    def __init__(self, CharacterName:str, Jump:int, Swim:int, Run:int, Drive:int) -> None:
        self.__CharacterName:str = CharacterName
        self.__Jump:int = Jump
        self.__Swim:int = Swim
        self.__Run:int = Run 
        self.__Drive:int = Drive

    def GetName(self):
        return self.__CharacterName
    
    # d
    def CalculateScore(self, EventType:str, Difficulty:int):
        # 4 event types
        # difference mappings
        
        skill_level = 0
        EventType = EventType.lower()
        if EventType == "jump":
            skill_level = self.__Jump
        elif EventType == "swim":
            skill_level = self.__Swim
        elif EventType == "run":
            skill_level = self.__Run
        elif EventType == "drive":
            skill_level = self.__Drive
            
        if skill_level >= Difficulty:
            return 100
        else:
            return 100-((Difficulty-skill_level)*20)
            



# b i
Group:list[EventItem] = [] # array of 5 EventItem
# b ii
Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))


# e i
Player01 = Character("Tarz", 5, 3, 5, 1)
Player02 = Character("Geni", 2, 2, 3, 4)


Player01Points, Player02Points = 0,0
# e ii
for event in Group:
    Player01Chance = Player01.CalculateScore(event.GetEventType(), event.GetDifficulty())
    Player02Chance = Player02.CalculateScore(event.GetEventType(), event.GetDifficulty())
    
    if Player01Chance > Player02Chance:
        print(f"{Player01.GetName()} has won the event {event.GetName()}")
        Player01Points = Player01Points + 1
    elif Player02Chance > Player01Chance:
        print(f"{Player02.GetName()} has won the event {event.GetName()}")
        Player02Points = Player02Points + 1
        
    elif Player01Chance == Player02Chance:
        print(f"The event {event.GetName()} resulted in a draw")
        
if Player01Points > Player02Points:
    print(f"{Player01.GetName()} has won with {Player01Points}")
elif Player02Points > Player01Points:
    print(f"{Player02.GetName()} has won with {Player02Points}")
elif Player01Points == Player02Points:
    print("The group was a draw")