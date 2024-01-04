#!/usr/bin/python3

try:
    x = int(input("Enter the firste number: "))
    y = int(input("Enter the second number: "))
    print("The result is ", x /y)
except (ZeroDivisionError, ValueError) as msg:
    print("Exception name : ", msg.__class__.__name__)
    print("Please enter valid input")
