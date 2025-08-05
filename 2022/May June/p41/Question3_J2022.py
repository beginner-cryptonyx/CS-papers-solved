# DECLARE QueueArray: ARRAY[0:9] OF STRING
QueueArray:list[str] = ["" for _ in range(10)]
head = 0 # INTEGER
tail = 0 # INTEGER
number_of_items = 0 # INTEGER

# FUNCTION Enqueue(BYREF QueueArray[] : STRING, BYREF HeadPointer : INTEGER, BYREF TailPointer : INTEGER, NumberItems : INTEGER, DataToAdd : STRING) RETURNS BOOLEAN
#     IF NumberItems = 10 THEN
#         RETURN FALSE
#     ENDIF
#     QueueArray[Tail] ← DataToAdd
#     IF TailPointer >= 9 THEN
#         TailPointer ← 0
#     ELSE
#         TailPointer ← TailPointer + 1
#     ENDIF
#     NumberItems ← NumberItems + 1
#     RETURN TRUE
# ENDFUNCTION

def Enqueue(DataToAdd) -> bool:
    global number_of_items, head, tail, QueueArray
    if number_of_items == 10:
        return False
    QueueArray[tail] = DataToAdd
    if tail >= 9:
        tail = 0
    else:
        tail = tail + 1
    number_of_items = number_of_items + 1
    return True


def Dequeue():
    global QueueArray, head, tail, number_of_items
    if number_of_items <=  0:
        return "FALSE"
    
    return_element = QueueArray[head]
    if head >= 9:
        head = 0
    else: 
        head = head +1 
    number_of_items = number_of_items - 1
    return return_element


for _ in range(11):
    value = input("Enter a string value: ")
    res = Enqueue(value)
    if res:
        print(f"{value} was added successfully to the queue")
    else:
        print(f"{value} could not be added to the queue")
    
print(Dequeue())
print(Dequeue())