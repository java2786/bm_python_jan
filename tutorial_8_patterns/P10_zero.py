"""
Zero pattern using stars


* * * *
*     *
*     *
*     *
* * * *



11 12 13 14 
21       24 
31       34 
41       44 
51       54 
61       64 
71       74 
81 82 83 84 


* * * * 
*     * 
*     * 
*     * 
*     * 
*     * 
*     * 
* * * * 


"""


num = 5

for r in range(1, 2*num):
    for c in range(1, num+1):
        if(r==1 or c==1 or r == 2*num-1 or c == num):
            print(f"* ",end="")
        else:
            print(f"  ",end="")
    print()


