#!/usr/bin/python3
# By Ekeno

class Test:
    '''various places to declare static variables'''
    a = 10 # Outside constructor

    def __init__(self):
        #inside constructor using class name
        Test.b = 20

    def mi(self):
        Test.c = 30
    
    @classmethod
    def m2(cls):
        #inside class method using cls or classname
        cls.d = 40
        Test.e = 50

    @staticmethod
    def m3():
        #inside static method using classname
        Test.f = 60

print(Test.__dict__)
print()

t1 = Test()
print(Test.__dict__)
print()

t2 = Test()
t2.mi()
print(Test.__dict__)
print()

Test.m2()
print(Test.__dict__)
print()

Test.m3()
print(Test.__dict__)
print()

#outside the class using classname
Test.g = 70
print(Test.__dict__) 
