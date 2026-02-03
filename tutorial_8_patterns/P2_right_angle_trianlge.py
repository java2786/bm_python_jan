"""
Triangle pattern using stars

* 
* * 
* * * 
* * * *

"""


num = 4

for r in range(num):
    # print(r+1)

    for c in range(r+1):
        print("* ", end="")
    print()