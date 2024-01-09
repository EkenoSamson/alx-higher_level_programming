#!/usr/bin/python3
"""Module for file writing"""


def write_file(filename="", text=""):
    """function that write text to file"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
