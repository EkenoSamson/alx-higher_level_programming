#!/usr/bin/python3
# By Ekeno

class Test:
    '''How to access static variables'''
    a = 10
    
    #inside constructor by using self or classname
    def __init__(self):
        print(self.a)
        print(Test.a)

    #inside instance method by using self or classname
    def m1(self):
        print(self.a)
        print(Test.a)

    #inside class method by using cls or classname
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    #inside static method by using classname
    @staticmethod
    def m3():
        print(Test.a)

t = Test()
print()

t.m1()
print()

t.m2()
print()

t.m3()
print()

#outside class
print(t.a)
print(Test.a)

