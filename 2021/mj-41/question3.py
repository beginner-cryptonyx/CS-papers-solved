# a
class TreasureChest():
    def __init__(self, question:str, answer:str, points:int) -> None:
        # string self.__question
        # string self.__answer
        # integer self.__points
        self.__question: str = question
        self.__answer: str = answer
        self.__points: int = points
    
    #c i     
    def getQuestion(self) -> str:
        return(self.__question)
    
    # c ii
    def checkAnswer(self, answer:str) -> bool:
        if answer == self.__answer:
            return True
        return False
    
    # c iii
    def getPoints(self, attempt_count:int) -> int:
        if attempt_count > 4 or attempt_count < 1:
            return 0
        return self.__points//attempt_count #this is bad logic, for 3 and 4 attempts it should be divided by 4, stick to if statements and de prioritize writing "slick code"
    

# b
# arrayTreasure ARRAY of TreasureChest
arrayTreasure:list[TreasureChest] = []
def readData() -> None:
    try:
        with open("./2021/mj-41/TreasureChestData.txt", 'r') as f:
            content = f.read()
            content = content.split('\n')
            count = 0
            question = ""
            answer = ""
            points = 0
            for line in content:
                count +=1
                match count:
                    case 1:question = line
                    case 2: answer = line
                    case 3:
                        points = int(line)
                        arrayTreasure.append(TreasureChest(question, answer, points))
                        
                if count == 3:
                    count = 0
    except FileNotFoundError:
        print("File not able to be found")
        
        
# c iv
readData()

question_number = -1
while question_number < 1 or question_number > 5:
    question_number = int(input("Enter a number between 1 to 5 to get a question: "))

Treasure = arrayTreasure[question_number-1]

print(Treasure.getQuestion())

correct = False
attempts = 0
while not correct:
    answer = input("answer: ")
    correct = Treasure.checkAnswer(answer)
    attempts = attempts + 1

points = Treasure.getPoints(attempts)

print(f"You have been awarded with {points} points!")
    