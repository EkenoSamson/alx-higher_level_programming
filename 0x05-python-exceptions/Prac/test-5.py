#!/usr/bin/python3

try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("The result: ", x / y)

except BaseException as msg:
    print("The type of except: ", type(msg))
    print("The type of except: ", msg.__class__)
    print("The name of exception: ", msg.__class__.__name__)
    print("The description: ", msg)
