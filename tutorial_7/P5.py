"""
Input a number and count how many times each digit (0–9) appears.
    -> 8987898778
"""

# num = 8987898778
# 8 - 5, 9 - 2, 7 - 3

num = 38018
zero_count = 0
one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0
six_count = 0
seven_count = 0
eight_count = 0
nine_count = 0

while num>0:
    ld = num % 10       
    num = num // 10     

    if ld == 0:
        zero_count = zero_count + 1 
    elif ld == 1:
        one_count = one_count + 1 
    elif ld == 2:
        two_count = two_count + 1 
    elif ld == 3:
        three_count = three_count + 1 
    elif ld == 4:
        four_count = four_count + 1 
    elif ld == 5:
        five_count = five_count + 1 
    elif ld == 6:
        six_count = six_count + 1 
    elif ld == 7:
        seven_count = seven_count + 1 
    elif ld == 8:
        eight_count = eight_count + 1 
    elif ld == 9:
        nine_count = nine_count + 1 

if zero_count>0:
    print(f"0 occurrance {zero_count}")
if one_count>0:
    print(f"1 occurrance {one_count}")
if two_count>0:
    print(f"2 occurrance {two_count}")
if three_count>0:
    print(f"3 occurrance {three_count}")
if four_count>0:
    print(f"4 occurrance {four_count}")
if five_count>0:
    print(f"5 occurrance {five_count}")
if six_count>0:
    print(f"6 occurrance {six_count}")
if seven_count>0:
    print(f"7 occurrance {seven_count}")
if eight_count>0:
    print(f"8 occurrance {eight_count}")
if nine_count>0:
    print(f"9 occurrance {nine_count}")
