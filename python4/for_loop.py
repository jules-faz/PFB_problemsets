my_list = [101,2,15,22,95,33,2,27,72,15,52]
sorted_list = sorted(my_list)
even_list = 0
odd_list = 0
for num in sorted_list:
    #print(num)
    if num%2==0:
        even_list += num
    else:
        odd_list += num
print(even_list)
print(odd_list)