"""
CORRECTIONS

OVERALL ---- 34/34

a - 4/4
    3/3
b - 5/5
    1/1
c - 4/4
    5/5
d - 5/5
e - 3/3
    2/2
    2/2
"""

# a i 
class Horse:
    # private Name as String
    # private MaxFenceHeight as Integer
    # private PercentageSuccess as Integer
    
    def __init__(self, Name:str, MaxFenceHeight:int, PercentageSuccess:int) -> None:
        self.__Name:str = Name #string 
        self.__MaxFenceHeight:int = MaxFenceHeight # Integer
        self.__PercentageSuccess:int = PercentageSuccess # Integer

    # a ii 
    def GetName(self) -> str:
        return self.__Name
    def GetMaxFenceHeight(self) -> int:
        return self.__MaxFenceHeight
    
    # d
    def Success(self, height:int, risk:int) -> float:
        if height > self.__MaxFenceHeight:
            return 0.2 * self.__PercentageSuccess
        else:
            risk_factor = -1
            if risk == 1:
                risk_factor = 1
            elif risk == 2:
                risk_factor  = 0.9
            elif risk == 3:
                risk_factor  = 0.8
            elif risk == 4:
                risk_factor  = 0.7
            elif risk == 5:
                risk_factor  = 0.6
            
            return risk_factor * self.__PercentageSuccess
# b i 

Horses:list[Horse] = [] # List of (2) Horse
Horses.append(Horse("Beauty", 150, 72))
Horses.append(Horse("Jet", 160, 65))
for horse in Horses:
    print(horse.GetName())

# b ii
"""
Beauty
Jet
"""

# c i 
class Fence:
    # private Height as Integer
    # private Risk as Integer
    def __init__(self, Height:int, Risk:int) -> None:
        self.__Height = Height # Integer between 70 and 180 inclusive
        self.__Risk = Risk # Integer between 1 and 5
        
    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk
    
# c ii

Course:list[Fence] = []

for i in range(4):
    height = -1
    risk = -1
    
    while height < 70 or height > 180:
        height = int(input(f"Input the height for fence {i+1} (70-180): "))
        
    while risk < 1 or risk > 5:
        risk = int(input(f"Input the risk for fence {i+1} (1-5): "))
        
    current_fence = Fence(height, risk)
    Course.append(current_fence)
    
# e i and ii
horse_average = []
for i in range(len(Horses)):
    horse = Horses[i]
    total = 0
    for j  in range(len(Course)):
        course = Course[j]
        success = horse.Success(course.GetHeight(), course.GetRisk())
        print(f'The horse {horse.GetName()} at fence {j} has a {success}% chance of success')
        total += success
        
    average = total/len(Course)
    horse_average.append(average)
    print(f"The horse {horse.GetName()} has an average {average}% chance of jumping over all four fences")
    
best_horse = ""
best_average = 0

for i in range(len(horse_average)):
    if horse_average[i] > best_average:
        best_average = horse_average[i]
        best_horse = Horses[i].GetName()
        
print(f"{best_horse} has the highest average chance of success")



# e iii
"""
Beauty
Jet
Input the height for fence 1 (70-180): 152
Input the risk for fence 1 (1-5): 5
Input the height for fence 2 (70-180): 121
Input the risk for fence 2 (1-5): 1
Input the height for fence 3 (70-180): 130
Input the risk for fence 3 (1-5): 3
Input the height for fence 4 (70-180): 145
Input the risk for fence 4 (1-5): 4
The horse Beauty at fence 0 has a 14.4% chance of success
The horse Beauty at fence 1 has a 72% chance of success
The horse Beauty at fence 2 has a 57.6% chance of success
The horse Beauty at fence 3 has a 50.4% chance of success
The horse Beauty has an average 48.6% chance of jumping over all four fences
The horse Jet at fence 0 has a 39.0% chance of success
The horse Jet at fence 1 has a 65% chance of success
The horse Jet at fence 2 has a 52.0% chance of success
The horse Jet at fence 3 has a 45.5% chance of success
The horse Jet has an average 50.375% chance of jumping over all four fences
Jet has the highest average chance of success
"""