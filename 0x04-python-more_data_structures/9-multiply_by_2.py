#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s_dictionary = a_dictionary.copy()
    for key in s_dictionary:
        s_dictionary[key] = (s_dictionary[key]) * 2
    return (s_dictionary)
