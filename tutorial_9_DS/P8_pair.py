# user_movies = {"Bahubali", "AAA", "Bahubali", "AAA""Bahubali", "AAA"}


# items = {
#     key: value
# }

items = {
    "pizza": 70,
    "burger": 50,
    "samosa": 15
}
items["tea"] = 10

items['burger'] = 55
print(f"Type: {type(items)}")
print(items)

print(f"Burger price: {items['burger']}")
print(f'Tea price: {items["tea"]}')

for k in items:
    print(f"{k} -> {items[k]}")

for v in items.values():
    print(f"{v}")
    