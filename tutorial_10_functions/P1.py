""" 
Function is reusable code
organised content
maintenance
"""



def greet():
    print("Welcome")
    
# Trigger - Calling - Execute
greet()


def greet_user(name):
    print("Welcome",name)
    
# Trigger - Calling - Execute
greet_user("Ramesh")


def findStudent(roll):
    # find student from databse or file
    name = "Ramesh"
    marks = 72
    return (name,marks)
    
std = findStudent(123)
# std[1] = 77
print(std[0])
print(std[1])




def add(*args):
    print(f"Type: {type(args)}")
    sum = 0
    for i in range(len(args)):
        sum = sum + args[i]
    return sum 

print(add(4))


def printTicket(**kwargs):
    print(f"Type: {type(kwargs)}")
    for key in kwargs:

        print(f"\t{key} -> {kwargs[key]}")


printTicket(name="Ramesh", date="11/02/2026", movie="Bahubali")
printTicket(train_name="Rajdhani", from_city="Jaipur", to_city="Pune", price=560, category="2AC")