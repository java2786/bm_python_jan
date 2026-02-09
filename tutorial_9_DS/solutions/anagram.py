#anagrams
# -same characters 
# -same length 

fw  = "listen"
sw = "silent"

print(sorted(fw))
print(sorted(sw))


if sorted(fw) == sorted(sw) :
    print("the strings are anagrams ")
    
else:
    print(" the strings are not anagrams")

