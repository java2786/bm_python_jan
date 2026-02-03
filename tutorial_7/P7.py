# Convert a binary number to decimal manually (no bin() function).


# sum = sum + find last digit * 2^count

num = 1010
counter = 0
sum = 0

while num>0:
    ld = num % 10
    num = num // 10
    
    sum = sum + ((2**counter) * ld)
    counter = counter + 1
print(sum)