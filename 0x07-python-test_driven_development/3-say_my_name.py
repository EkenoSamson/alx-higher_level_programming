#!/usr/bin/python3
"""
This file contains one function.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name of a person.

    Args:
        first_name : first name of the person
        last_name : last name of a person
    Raise:
        TypeError: if the argument is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
