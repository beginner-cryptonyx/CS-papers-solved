global StackVowel, StackConsonant
StackVowel = []  # ARRAY[0:99] OF STRING
StackConsonant = []  # ARRAY[0:99] OF STRING

global VowelTop, ConsonantTop
VowelTop = 0  # INTEGER
ConsonantTop = 0  # INTEGER


def PushData(letter) -> None:
    global VowelTop, ConsonantTop
    if letter in ["a", "e", "i", "o", "u"]:
        if VowelTop == 99:
            print("Error: Vowel stack is full")
        else:
            VowelTop += 1
            StackVowel.append(letter)

    else:
        if ConsonantTop == 99:
            print("Error: Consonant stack is full")
        else:
            StackConsonant.append(letter)
            ConsonantTop += 1


def ReadData():
    target_file = "2023\October November\p42\StackData.txt"
    try:
        with open(target_file, "r") as f:
            file_content = f.read()
            file_content = file_content.split("\n")
            for letter in file_content:
                PushData(letter)
            f.close()
    except Exception as e:
        print(f"Error: {e}")


def PopVowel():
    global VowelTop
    global StackVowel
    if VowelTop == 0:
        print("no data")
    else:
        VowelTop -= 1
        return StackVowel.pop()


def PopConsonant():
    global ConsonantTop
    global StackConsonant
    if ConsonantTop == 0:
        print("no data")
    else:
        ConsonantTop -= 1
        return StackConsonant.pop()

ReadData()
popped = ''
for _ in range(5):
    cmd = input("What do you want to pop? (vowel|consonant): ")
    if cmd.lower() == 'vowel':
        popped = f"{popped}{PopVowel()}"
    elif cmd.lower() == 'consonant':
        popped = f"{popped}{PopConsonant()}"

print(popped)