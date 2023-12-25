#!/usr/bin/python3

class Test:
    def __init__(self):
        print("Address of object pointed by self:", id(self))

k = Test()
print("Address pf object pointed by self:", id(k))
