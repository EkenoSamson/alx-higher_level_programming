#!/usr/bin/python3
# Introducing inheritance

class P:
    a = 10
    def __init__(self):
        print("Parent Constructor")
        self.b = 20

    def m1(self):
        print("Parent Instance method")

    @classmethod
    def m2(cls):
        print("Parent class method")

    @staticmethod
    def m3():
        print("Parent static method")


class C(P):
    pass

child = C()
print(" A = ", child.a)
child.m1()
child.m2()
child.m3()
