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
    Raises:
        TypeError - if width or height is not an integer.
        ValueError - if both are less than zero.
    """

    def __init__(self, width=0, height=0):
        """ create the object """
        self.width = width
        self.height = height

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
