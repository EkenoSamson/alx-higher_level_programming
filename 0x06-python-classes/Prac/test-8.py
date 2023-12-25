#!/usr/bin/python3
# By Ekeno

class Test:
    def __init__(self):
        print("No argument constructor")

    def __init__(self, x):
        print("One argument constructor")

t1 = Test()
t2 = Test(10)


