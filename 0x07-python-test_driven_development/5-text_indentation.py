#!/usr/bin/python3
"""
This module contains a function theat prints text encountering . or ? or :
"""


def text_indentation(text):
    """
    Prints a text with 2 newlines after each encounter

    Args:
        text - text to inspect.

    Raise:
        TypeError - if the text is not a string.
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    count = 0
    for char in text:
        if char == "." or char == "?" or char == ":":
            print(char)
            print()
            count += 2
            char = text[count]
        else:
            print(char, end="")
            count += 1
