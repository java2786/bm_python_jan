"""
Triangle pattern using stars

1 
2 2 
3 3 3 
4 4 4 4

"""


num = 4

# for r in range(num):
#     # print(r+1)

#     for c in range(1,r+2):
#         print(f"{c} ", end="")
#     print()


for r in range(1,num+1):

    for c in range(1,r+1):
        print(f"{r} ", end="")
    print()