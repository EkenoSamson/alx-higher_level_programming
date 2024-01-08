#!/usr/bin/python3
# By Ekeno

def safe_print_list_integers(my_list=[], x=0):
    t = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        t += 1
    print()
    return (t)
