#!/usr/bin/python3
# By Ekeno

class Test:
    """How to change instance varibales"""
    def __init__(self):
        self.a = 4
        self.b = 7

t1 = Test()
t1.a = 999
t1.b = 878
print("t1: ", t1.a, t1.b)

t2 = Test()
print(t2.__dict__)

