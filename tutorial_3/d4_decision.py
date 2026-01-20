# Find smaller number 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# a<b , a>b , a==b

if a<b:
    print("First")
    print(f"{a} is smaller than {b}")

elif a>b:
    print("second")
    print(f"{b} is smaller than {a}")

# elif a==b:
else:
    print("third")
    print(f"{b} is same as {a}")


print("Bye Bye")