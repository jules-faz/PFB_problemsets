#!/usr/bin/eny python3
set1 = {3, 14, 15, 9, 26, 5, 35, 9}
set2 = {60, 22, 14, 0, 9}

print(set1)
print(set2)

#intersection
intersection = set1 & set2
print(intersection)

#difference
difference = set1 - set2
print(difference)

#union
union = set1 | set2
print(union)

#symmetrical difference
symmetrical_difference = set1 ^ set2
print(symmetrical_difference)
