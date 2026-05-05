# a
global Queue, HeadPointer, TailPointer
Queue: list[str] = ["" for _ in range(50)]  # global list of 50 string elements
HeadPointer: int = -1  # global integer
TailPointer: int = 0  # global integer

# tail pointer points to NEXT FREE SPACE

# a ii


def Enqueue(value: str):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 51:
        print("Queue is full")
    else:
        Queue[TailPointer] = value
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0


# a iii


def Dequeue() -> str:
    global Queue, HeadPointer, TailPointer
    if HeadPointer >= TailPointer:
        print("Queue is empty")
        return "empty"
    else:
        return_value = Queue[HeadPointer]
        HeadPointer += 1
        return return_value


# b
def ReadData():
    try:
        file = open("2023/on_41/QueueData.txt", "r")
        EOF = False
        while not EOF:
            line = file.readline().strip()
            if line == "":
                EOF = True
            else:
                Enqueue(line)

        file.close()
    except IOError or FileNotFoundError:
        print("File was not found")


# c i
class RecordData:
    # ID as String
    # Total as Integer
    def __init__(self) -> None:
        self.ID: str = ""  # string
        self.Total: int = 0  # Integer


# c ii
global Records, NumberRecords
Records: list[RecordData]  # global Array of 50 RecordData
NumberRecords: int = 0  # global Integer
Records = [RecordData() for _ in range(50)]


# c iii
def TotalData():
    global Records, NumberRecords

    DataAccessed: str
    Flag: bool
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1

    else:
        for x in range(0, NumberRecords):
            if Records[x].ID == DataAccessed:
                Records[x].Total = Records[x].Total + 1
                Flag = True
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords = NumberRecords + 1


# d
def OutputRecords():
    global NumberRecords, Records
    for i in range(NumberRecords):
        record = Records[i]
        print(f"ID {record.ID} Total {record.Total}")


# e i

ReadData()
for i in range(HeadPointer, TailPointer):
    TotalData()
OutputRecords()


# e ii
"""
ID 1234 Total 1
ID 1568 Total 1
ID 9512 Total 2
ID 4567 Total 4
ID 8512 Total 6
ID 4125 Total 3
ID 9651 Total 1
ID 4851 Total 1
ID 2520 Total 2
ID 3265 Total 1
ID 8966 Total 1
"""
