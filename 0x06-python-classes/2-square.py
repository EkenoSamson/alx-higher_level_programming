#!/usr/bin/python3
""" class square """


class Square:
    """
    class definition

    Args: size - size of a square
    """
    def __init__(self, size=0):
        """ Initialising the variables"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
