# Find if all prime numbers from 1 to N
n = 50
for num in range(2, n+1):
    is_prime = True
    for i in range(2, num//2 + 1):
        # print(i)
        if num%i==0:
            # print(num,"is divisible by",i)
            is_prime = False
            break 

    if(is_prime == True):
        print(f"{num} is prime")
    # else:
    #     print(f"{num} is not prime")