#!/usr/bin/python3
"""
The module contains the class Rectangle
"""


class Rectangle:
    """
    Rectangle blueprint

    Args:
        width - one side of the rectangle.
        height - one side of the rectangle.
        number_of_instances -
    Raises:
        TypeError - if width or height is not an integer.
        ValueError - if both are less than zero.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ create the object """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """width retriever"""
        return self.__width

    @width.setter
    def width(self, value):
        """width mutator"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height retriver"""
        return self.__height

    @height.setter
    def height(self, value):
        """height mutator"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rec += "#"
            if i < (self.__height - 1):
                rec += "\n"
        return (rec)

    def __repr__(self):
        """return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
