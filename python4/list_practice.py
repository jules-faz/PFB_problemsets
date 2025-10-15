my_list = ['a', 'bb', 'ccc']
list_copy = my_list
list_copy.append("dddd")
print(my_list)
list_copy2 = my_list.copy()
print(my_list)
list_copy2.append("eeeee")
print(my_list)
