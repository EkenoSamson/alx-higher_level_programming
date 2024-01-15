#!/usr/bin/python3
Phone = __import__('samsung').Phone

p1 = Phone(80, 3)
print(p1.__dict__)
x = p1.__class__.__dict__

for i in x:
    print(i)


print(str(p1))
print(repr(p1))
print(p1)
print(p1.weight())
