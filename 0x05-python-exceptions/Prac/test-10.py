#!/usr/bin/python3
try:
    print("Try")
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")

