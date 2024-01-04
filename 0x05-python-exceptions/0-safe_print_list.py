#!/usr/bin/python3
#By Ekeno

def safe_print_list(my_list = [], x = 0):
    i = 0
    while (x != 0):
        try:
            print(my_list[i], end="")
            x -= 1
            i += 1
        except IndexError:
            i -= 1
    print()
    return (i)
