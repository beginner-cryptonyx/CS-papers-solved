"""
CORRECTIONS

OVERALL ---- 15/17

a - 1/1
b - 4/4
c - 2/3
d - 6/6
    1/1
    1/2
"""

# a
global QueueData, QueueHead, QueueTail
QueueData: list[str] = ["" for _ in range(20)]  # global array of 20 strings
QueueHead: int = -1
QueueTail: int = -1


# b
def Enqueue(value: str) -> bool:
    global QueueData, QueueHead, QueueTail
    # q is full
    if QueueTail == 19:
        return False
    else:
        QueueTail += 1
        QueueData[QueueTail] = value
        if QueueHead == -1:
            QueueHead = 0
        return True


# c
def Dequeue() -> str:
    global QueueData, QueueHead, QueueTail
    # q is empty
    if QueueHead > QueueTail or QueueHead == -1:
        return "false"
    else:
        return_value = QueueData[QueueHead]
        QueueHead += 1
        return return_value


# debug
def debug():
    global QueueData, QueueHead, QueueTail
    print("head", QueueHead)
    print("tail", QueueTail)
    print("raw queue", QueueData)
    for i in range(QueueHead, QueueTail):
        print(QueueData[i], end="|")


# d i
def StoreItems():
    for _ in range(10):
        code = input("enter a code: ")

        # check digit
        check_digit = code[6]
        code = code[0:6]

        # check digit validation
        result = (
            int(code[0])
            + int(code[2])
            + int(code[4])
            + 3 * (int(code[1]) + int(code[3]) + int(code[5]))
        )
        result = str(result // 10)
        if result == "10":
            result = "X"
        # print(f"code: {code} | check digit: {check_digit} | real check digit: {result}")
        
        if result == check_digit:
            res = Enqueue(code)
            if res:
                print("The item was inserted")
            else:
                print('Queue is full')      

# d ii
StoreItems()
res = Dequeue()
if res == "false":
    print("Queue is empty")
else:
    print(res)

# d iii
"""
enter a code: 999999X
The item was inserted
enter a code: 1251484
The item was inserted
enter a code: 5500212
The item was inserted
enter a code: 0033585
enter a code: 9845788
The item was inserted
enter a code: 6666666
enter a code: 3258746
enter a code: 8111022
The item was inserted
enter a code: 7568557
The item was inserted
enter a code: 0012353
999999
"""
