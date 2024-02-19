# Area of a circle
import math


def area_circle():
    radius = float(input("Enter radius: "))
    area = math.pi * radius * radius
    print("The area of the circle is {} m^2".format(area))



area_circle()
