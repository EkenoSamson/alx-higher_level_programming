#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # reverse the list
    my_list.reverse()

    # print the elements
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
