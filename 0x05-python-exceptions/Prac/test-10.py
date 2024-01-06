#!/usr/bin/python3
#case 1: Exception raised and landlord
try:
    print("Try")
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")

