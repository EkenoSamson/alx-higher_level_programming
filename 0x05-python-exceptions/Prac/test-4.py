#!/usr/bin/python3
#exception type

try:
    print(10/0)
except ZeroDivisionError as msg:
    print("The type of exception: ", type(msg))
    print("The type of exception: ", msg.__class__)
    print("The exception class name: ", msg.__class__.__name__)
    print("The description of exception: ", msg)
