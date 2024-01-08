#!/usr/bin/python3
# By Ekeno

def safe_print_division(a, b):
    try:
        r = a/b
    except (ZeroDivisionError, ValueError):
        r = None
    finally:
        print("Inside result: {}".format(r))
    return (r)
