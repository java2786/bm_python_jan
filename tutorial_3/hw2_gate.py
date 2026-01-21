""" 
Find if user's age is valid for dirving license
    valid range => 18 years - 75 years
"""

age = int(input("Enter your age: "))
# if age>=18:
#     if age<=75:
#         print("valid")
#     else:
#         print("invalid")
# else:
#     print("invalid")


if age>=18 and age<=75:
    print("Valid")
else: 
    print("Invalid")
    
if age<18 or age>75:
    print("Invalid")
else: 
    print("Valid")