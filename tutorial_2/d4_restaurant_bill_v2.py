print("------ Welcome To Restaurant ------")
print("-------------our menu--------------")

pizza_price = 200
burger_price = 150
momos_price = 50
dosa_price = 70
print(f"1 Pizza:\tRs {pizza_price}/-")
print(f"2 Burger:\tRs {burger_price}/-")
print(f"3 Momos:\tRs {momos_price}/-")
print(f"4 Masala Dosa:\tRs {dosa_price}/-")

print()
pizza_quantity = int(input("Enter pizza quantity:\t"))
burger_quantity = int(input("Enter burger quantity:\t"))
momos_quantity = int(input("Enter momos quantity:\t"))
dosa_quantity = int(input("Enter dosa quantity:\t"))

print()
print("Item\tQuantity\tPrice\tTotal")
print("----------------------------------")
print(f"Pizza\t\t{pizza_quantity}\t{pizza_price}\t{pizza_price*pizza_quantity}")
print(f"Burger\t\t{burger_quantity}\t{burger_price}\t{burger_price*burger_quantity}")
print(f"Momos\t\t{momos_quantity}\t{momos_price}\t{momos_price*momos_quantity}")
print(f"Masala Dosa\t{dosa_quantity}\t{dosa_price}\t{dosa_price*dosa_quantity}")
print("----------------------------------")




print()
print(f"Total bill: {pizza_price*pizza_quantity + burger_price*burger_quantity + momos_price*momos_quantity + dosa_price*dosa_quantity}")
