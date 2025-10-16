#generate list with DNA data
DNA_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
Sorted_DNA_list = sorted(DNA_list, key=len)[::-1]
print(Sorted_DNA_list)



#for loop: print length and sequence separated by tab
for i in Sorted_DNA_list:
    print(i)