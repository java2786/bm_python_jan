# strong number = sum of factorials of each digit

for num in range(1, 100001):
    # num = 125
    copy = num 
    sum = 0
    while num > 0:
        ld = num % 10
        num = num // 10
        fact = 1
        for i in range(1, ld+1):
            fact = fact * i 

        sum = sum + fact 
        
    if(sum == copy):
        print(f"{copy} is strong number")
    
    