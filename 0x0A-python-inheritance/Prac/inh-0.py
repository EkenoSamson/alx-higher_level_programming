#!/usr/bin/python3
""" Specifying a superclass """

class A(object):
    def __init__(self, x):
        self.x = x

    def f(self):
        return 10 * self.x

class B(A):
    def g(self):
        return 1000 * self.x

print(A(5).f()) # 50
try:
    print(B().g())
except TypeError as msg:
    print(msg)

print(B(7).f()) # 70
print(B(7).g()) # 7000

try:
    print(A(3).g())
except AttributeError as msg:
    print(msg)

