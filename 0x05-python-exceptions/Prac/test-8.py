#!/usr/bin/python3

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("The result : ", (x / y))
except:
    print("Default except block : provide int value")
except ZeroDivisionError:
    print("ZeroDivisionError: Division by zero")
