#!/usr/bin/python3
#By Ekeno

class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom

    def __str__(self):
        return (str(self.num) + "/" + str(self.denom))

    def __add__(self, other):
        bott = self.denom * other.denom
        top = (self.num * other.denom) + (other.num * self.denom)
        return Fraction(top, bott)

    def __sub__(self, other):
        bott = self.denom * other.denom
        top = (self.num * other.denom) - (other.num * self.denom)
        return Fraction(top, bott)

    def __float__(self):
        return (self.num / self.denom)

    def inverse(self):
        return Fraction(self.denom, self.num)


a = Fraction(1,4)
b = Fraction(3, 4)
c = a + b
print(a)
print(float(a))
print(Fraction.__float__(c))
print(float(b.inverse()))
