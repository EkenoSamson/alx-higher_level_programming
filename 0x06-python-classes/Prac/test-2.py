#!/usr/bin/python3

class Test:
    def __init__(self):
        print("Constructor")

    def me(self, x = 0):
        print("X value is: ", x)

t = Test()
t.me(10)
