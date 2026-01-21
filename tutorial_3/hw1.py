# Triangle sides: find if it is right angle triangle 
"""
H^2 = P^2 + B^2

longest_side = H
other sides are B and P
"""

side_1 = 1
side_2 = 1
side_3 = 2
H = None 
P = None 
B = None 

# turnery --
# 
# H = True if (3>2) else False

# H = value_if_true if condition else value_if_false

# H = side_1 if side_1>side_2 else side_2
# H = side_3 if side_3>H else H

# H = (side_3 if side_3>side_1 else side_1) if (side_1>side_2) else (side_3 if side_3>side_2 else side_2)

if side_1 > side_2:
    if side_1 > side_3:
        H = side_1
        P = side_2
        B = side_3 
    else:
        H = side_3 
        P = side_1 
        B = side_2 
else:
    if side_2 > side_3:
        H = side_2 
        P = side_1 
        B = side_3
    else:
        H = side_3 
        P = side_1 
        B = side_2 

print(H)
print(B)
print(P)

if H*H == B*B + P*P:
    print("this is right angle triangle")
else:
    print("This is not right angle trianle")