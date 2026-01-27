# Count the digits of a given number          - 7834 => 4

num = 12345
num_copy = num
count = 0


while num>0:
    ld = num % 10
    num = num // 10
    count = count + 1

print(f"{num_copy} has {count} digits")