student = ["Ramesh", 21, 78.4] # [] -> list -> modify

student[2] = 81.9 # possible in list

print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Marks: {student[2]}")


# employee = "Ramesh", 34, 50000 # , separated values -> tuple -> not modify
employee = ("Ramesh", 34, 50000) # () -> tuple -> not modify
# employee[2] = 55000 # not possible in tuple
print(f"Name: {employee[0]}")
print(f"Age: {employee[1]}")
print(f"Marks: {employee[2]}")


print("="*15)
print(f"Type1: {type(student)}")
print(f"Type2: {type(employee)}")



