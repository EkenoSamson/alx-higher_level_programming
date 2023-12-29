#!/usr/bin/python3
# By Ekeno

class Test:
    '''How to delete instance variable'''
    def __init__(self):
        self.a = 10
        self.c = 20

    def remove(self):
        del self.c

t = Test()
t.remove()
print(t.__dict__)
