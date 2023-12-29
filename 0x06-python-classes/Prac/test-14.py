#!/usr/bin/python3
# By Ekeno

class Test:
    '''How to access static variable'''
    a = 10
    def __init__(self):
        Test.a = 20
    def m1(self):
        Test.a = 30

    @classmethod
    def m2(cls):
        cls.a = 40
        Test.a = 50

    @staticmethod
    def m3():
        Test.a = 60

t = Test()
print(t.a)

t.m1()
print(t.a)

t.m2()
print(t.a)

t.m3()
print(t.a)


Test.a = 70
print(t.a)

