# show last 4 characters

# first 4 chars name.upper + year

name = "vegetable"

print(f"First 3 chars: {name[0:3]}")

print(f"First 4 chars: {name[:4]}")

print(f"from 3: {name[3:]}")

print(f"Last 3: {name[-3:]}")

phone = "90988776"

print("*"*4, end="")
print("-", end="")
print("*"*4, end="")
print("-", end="")
print(f"{phone[-4:]}")