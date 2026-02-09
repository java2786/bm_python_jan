# Find total bill of 5 items - list 
items = []

num = int(input("Enter number of items: "))
total = 0
for i in range(num):
    price = int(input(f"Enter price of item #{i+1}: "))
    items.append(price)
    total = price + total
    
print(items)
print(f"Total {total}")