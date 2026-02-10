# Find if given number is prime of not

def is_prime_func(num):
    print("Calculating",num)
    flag = True 

    for i in range(2, num//2 + 1):
        # print(i)
        if num%i==0:
            flag = False
            break 
    return flag



