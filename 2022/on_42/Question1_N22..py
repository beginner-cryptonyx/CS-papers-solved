"""
# CORRECTIONS
OVERALL ------ 21/23

a - 2/3 - should be # Integer 100 by 2 elements
b - 3/3
c - 5/5 - tho missed print("added")
d - 2/2
e - 5/5
f - 3/3
g - 1/1
    0/1 - again, the added thing

"""



# a
global NumberOfJobs, Jobs
Jobs:list[list[int]] = [[] for _ in range(99)]# Array of 200 integers

# b
def Initialise():
    global NumberOfJobs, Jobs
    NumberOfJobs = 0
    for row in range(100):
        Jobs[row] = [-1,-1]
        
        
# c
def AddJob(number:int, priority:int):
    global NumberOfJobs, Jobs
    if priority > 10 or priority < 1 or NumberOfJobs == 100:
        print("Not Added")
    else:
        Jobs[NumberOfJobs] = [number, priority]
        # should have been there print("Added")
        NumberOfJobs = NumberOfJobs + 1
    
# d 
Initialise()
for job in [[12,10], [526, 9], [33, 8], [12, 9], [78, 1]]:
    AddJob(job[0], job[1])
    

# print(Jobs, NumberOfJobs)

# e
def InsertionSort():
    global NumberOfJobs, Jobs
    for i in range(1, NumberOfJobs):
        j = i
        key = Jobs[i]
        while j > 0 and Jobs[j-1][1] >= key[1]:
            Jobs[j] = Jobs[j-1]
            j = j - 1
        Jobs[j] = key
# InsertionSort()
# f
def PrintArray():
    global NumberOfJobs, Jobs
    for i in range(NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")


# g
InsertionSort()
PrintArray()