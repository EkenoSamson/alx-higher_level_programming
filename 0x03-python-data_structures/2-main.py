#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = len(my_list)
new_element = 23
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
