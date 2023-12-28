#!/usr/bin/python3
#By Ekeno

class Coordinate(object):
    """ Class co-ordinate is for defining points on a cartesian plane"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.x - other.x) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    def __str__(self):
        return ("<" + str(self.x) + ", " + str(self.y) + ">")

c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.x)
print(c.y)
print(c.distance(origin))
print(c)
print(Coordinate)
print(type(c))
print(isinstance(c, Coordinate))
