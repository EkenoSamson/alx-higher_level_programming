#!/usr/bin/python3
"""
Module contains class Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle.
    """
    def __init__(self, size):
        """ Initialise size argument"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area of a square"""
        return (self.__size ** 2)
