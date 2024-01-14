#!/usr/bin/python3
"""
This module contains the function print_square
"""


def print_square(size):
    """
    Prints a square using #.

    Args:
        size - size of the square.

    Raise:
        TypeError - if size is not an integer.
        ValueError - if size is less than zero.
    """
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    elif type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
