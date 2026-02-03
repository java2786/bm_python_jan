"""
Square pattern using stars


. . . .
. . . .
. . . .
. . . .


* * * *
* * * *
* * * *
* * * *

# # # #
# # # #
# # # #
# # # #


"""


num = 8

for i in range(num):
    for j in range(num):
        print(f"* ", end="")
    print()