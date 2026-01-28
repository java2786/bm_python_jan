# Convert a decimal number to binary manually (no bin() function).

num = 765
result = ""
# print(bin(num))

# divide until num becomes 0
# and combine all the remainder values to get binary

while num>0:
    rem = num % 2
    num = num // 2
    # print(rem)
    # result = result + str(rem) # "0011"
    result = str(rem) + result  # "1100"
    
print(result)

