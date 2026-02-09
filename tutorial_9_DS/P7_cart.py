#  {} -> container to hold multiple unique values
cart = {
    "mango", "book", "pen", "book", 
    "pen", "mango", "milk"
    }

print(cart)

# print(f"First value: {cart[0]}")

for item in cart:
    print(item)
    
    
ott_movies = {"Bahubali", "Pushpa", "RRR", "India", "AAA"}
user_movies = {"Bahubali", "Bahubali", "AAA", "Bahubali", "AAA", "AAA", "Bahubali", "Bahubali", "AAA"}

print(user_movies)
print(f"Recommendation: {ott_movies.difference(user_movies)}")