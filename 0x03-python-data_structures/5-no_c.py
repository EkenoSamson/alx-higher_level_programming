#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    string_list = [i for i in string_list if (i != "c" and i != "C")]
    return (''.join(string_list))
