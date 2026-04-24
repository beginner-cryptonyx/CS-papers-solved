# a 
def Unknown(x:int, y:int) -> int:
    if x < y:
        print(x+y)
        return (Unknown(x+1, y) * 2)
    elif x == y:
        return 1
    else:
        print(x + y)
        return (Unknown(x-1, y) // 2)
    
    
# b i 
calling = [(10,15), (10,10), (15,10)]
for x,y in calling:
    print(f"Calling {x} and {y} as parameters to the Unknown() function")
    result = Unknown(x,y)
    print(f"Result was {result}")
    
    
    
# c - 
# ultimately it is 2^(y-x)

def IterativeUnknown(x:int, y:int) -> int:
    result = 1
    while True:
        if x < y:
            print(x+y)
            result = result * 2
            x = x + 1
        elif x == y:
            break
        else:
            print(x+y)
            result = result // 2
            x = x - 1
    return result
            
            
            
            
            
# d i 
for x,y in calling:
    print(f"Calling {x} and {y} as parameters to the IterativeUnknown() function")
    result = IterativeUnknown(x,y)
    print(f"Result was {result}")