#!/usr/bin/python3
"""
Module contains class BaseGeometry.
"""


class BaseGeometry(object):
    """
    Contains area() and integer_validator methods
    """
    def area(self):
        """ Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """" validates value """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
