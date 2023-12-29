#!/usr/bin/python3
# By Ekeno

class Robot:
    """
    Robot information
    """
    pass

'''if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)
'''

x = Robot()
y = Robot()

#Not the best way to declare and initialise attributes
x.name = "Marvin"
x.build_year = "1979"
y.name = "Caliban"
y.build_year = "1993"
print(x.name)
print(y.build_year)

print(x.__dict__)
print(y.__dict__)
Robot.brand = "Kuka"
print(x.brand)

