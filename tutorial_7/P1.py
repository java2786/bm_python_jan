# Find if given number is prime of not

num = 47
is_prime = True 
# print(f"{num} is prime")
# print(f"{num} is not prime")

""" 
# rules
    number should not be divisible by 2 to N-1 or N/2
    num = 47
    2,3,4,5,6,..., 43,44,45,46
"""

for i in range(2, num//2 + 1):
    # print(i)
    if num%i==0:
        print(num,"is divisible by",i)
        is_prime = False
        break 

if(is_prime == True):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")