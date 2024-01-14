#!/usr/bin/python3
"""
It has one function.
"""


def add_integer(a, b=98):
    """
    Return sum of integer a and b

    Args:
        a: first number
        b: second number

    Raises:
        TypeError: if any of the argument is not an integer or float
    """

    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
