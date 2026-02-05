fruits = ["Banana", "Mango", "Watermelon", "Guava"]

print(f"Value: {fruits}")
print(f"Type: {type(fruits)}")

print(f"First: {fruits[0]}")

print(f"Last: {fruits[-1]}")
print(f"Last: {fruits[len(fruits)-1]}")


# CRUD

friends = ["Ramesh", "Suresh", "Dinesh"]
print("="*20)

print("CRUD - Create")
friends.append("Ganesh")

print("CRUD - Update")
friends[1] = "Mukesh"

print("CRUD - Delete")
# friends.remove("Mahesh")
friends.remove("Mukesh")

print("CRUD - Read")
for i in range(len(friends)):
    print(friends[i])
