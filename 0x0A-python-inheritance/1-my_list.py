#!/usr/bin/python3
"""
The nodule contains a class MyList that inherits from List.
"""


class MyList(list):
    """
    Inherits from list class.
    """
    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted (ascending).
        """
        print(sorted(self))
