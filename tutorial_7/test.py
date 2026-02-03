num = int(input("Enter number of students: "))
min = 10000000
max = 0
total = 0
above_avg = 0



for i in range(num):
    score = int(input(f"Enter score of student {i+1}: "))
    if score > max:
        max = score 
    if score < min:
        min = score 
    total = total + score 

print(f"Max: {max}")
print(f"Min: {min}")
print(f"Avg: {total/num}")
