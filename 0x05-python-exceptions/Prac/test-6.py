#!/usr/bin/python3

try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print("The result is ", x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Provide interger values only")
