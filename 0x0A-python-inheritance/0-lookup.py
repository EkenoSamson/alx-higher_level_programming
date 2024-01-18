#!/usr/bin/python3
"""
This module contains the function lookup.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    Args:
        obj - takes in the obj.
    """
    return dir(obj)
