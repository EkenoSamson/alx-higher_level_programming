#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni_list = []
    for item in my_list:
        if item not in uni_list:
            uni_list.append(item)
    return (sum(uni_list))
