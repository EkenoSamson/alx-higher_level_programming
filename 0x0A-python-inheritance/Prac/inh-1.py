#!/usr/bin/python3
""" Overriding methods """

class A(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        return 10 * self.x
    def g(self):
        return 100 * self.x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def f(self):
        return 1000 * self.x
    def g(self):
        return (super().g(), self.y)

a = A(5)
try:
    b = B(7)
except TypeError as m:
    print(m)
print(a.f()) # 50
print(a.g()) # 500
print(b.f()) # 7000
print(b.g()) # (700, 99)
