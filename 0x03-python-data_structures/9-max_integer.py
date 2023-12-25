#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    for i in my_list:
        for j in my_list:
            if i < j:
                i = j
    return (i)
