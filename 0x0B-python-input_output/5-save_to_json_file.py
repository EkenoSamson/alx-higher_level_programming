#!/usr/bin/python3
"""save object to a JSOn file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
