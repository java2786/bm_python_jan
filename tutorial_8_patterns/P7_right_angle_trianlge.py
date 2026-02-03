"""
Triangle pattern using stars

1 
1 2 
1 2 3 
1 2 3 4

"""


num = 4

# for r in range(num):
#     # print(r+1)

#     for c in range(1,r+2):
#         print(f"{c} ", end="")
#     print()


for r in range(1,num+1):

    for c in range(1,r+1):
        print(f"{c} ", end="")
    print()