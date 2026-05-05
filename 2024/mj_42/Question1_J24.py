"""
CORRECTIONS

OVERALL ---- 22/22

a - 6/6
b - 4/4
c - 6/6
    3/3
d - 1/1
    1/1
    1/1
"""

# c i 
def Play():
    global WordArray, NumberWords
    print(f"Main word: {WordArray[0]} | Answers: {NumberWords}")
    answer = ""
    correct = 0
    while answer != "no":
        answer = input("enter a word: ").lower()
        IsAnswer = False
        for i in range(len(WordArray)):
            if answer == WordArray[i]:
                IsAnswer = True
                WordArray[i] = ""
                correct += 1
        if IsAnswer:
            print(f"{answer} was an answer!")
        else:
            print(f"{answer} was not an answer")
    # c ii
    print(f"You have entered {correct*100/NumberWords}% of all possible answers")
    print("These are the other answers: ")
    for word in WordArray[1:]:
        if word != "":
            print(word)
# a 
global WordArray, NumberWords
WordArray: list[str] = []
NumberWords:int = 0

def ReadWords(file_name):
    global WordArray, NumberWords
    try:
        file = open(file_name, "r")
        line = file.readline().strip()
        WordArray.append(line)
        count = 0
        while True:
            line  = file.readline().strip()
            if line == "":
                break
            else:
                WordArray.append(line)
                count += 1
        NumberWords = count
        # d i
        Play()
    except IOError or FileNotFoundError:
        print("File was not found")
        
# b
filename = ""
while filename not in ["easy", "medium", "hard"]:
    filename = input("Enter difficult (easy, medium, hard): ").lower()

if filename == "easy":
    ReadWords("2024/mj_42/Easy.txt")
elif filename == "medium":
    ReadWords("2024/mj_42/Medium.txt")
elif filename == "hard":
    ReadWords("2024/mj_42/Hard.txt")


    

        
# d ii

"""
Enter difficult (easy, medium, hard): easy
Main word: house | Answers: 14
enter a word: she
she was an answer!
enter a word: out
out was not an answer
enter a word: no
no was not an answer
You have entered 7.142857142857143% of all possible answers
These are the other answers: 
hues
hose
hoes
shoe
sou
ohs
ose
oes
sue
use
hue
hoe
hes
"""

# d iii

"""
Enter difficult (easy, medium, hard): hard
Main word: fainted | Answers: 97
enter a word: fine
fine was an answer!
enter a word: fined
fined was an answer!
enter a word: idea
idea was an answer!
enter a word: no
no was not an answer
You have entered 3.0927835051546393% of all possible answers
These are the other answers: 
defiant
detain
fadein
nidate
anted
fated
tined
defat
feint
teind
entia
fetid
tenia
faint
fiend
tinea
adit
daft
defi
diet
dite
fain
fend
neif
tend
aide
date
deft
dine
edit
fane
feta
nide
tide
ante
deaf
deni
dint
fate
fiat
naif
nite
tied
anti
dean
dent
dita
fade
feat
find
neat
tain
tine
aft
and
ate
die
eat
fad
fen
fin
nit
tea
tin
aid
ane
dan
dif
eft
fan
fet
fit
tad
ted
ain
ani
def
din
end
fat
fid
nae
tae
ten
ait
ant
den
dit
eta
fed
fie
net
tan
tie
"""