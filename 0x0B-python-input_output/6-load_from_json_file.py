#!/usr/bin/python3
"""create object from a json file"""
import json


def load_from_json_file(filename):
    """create an object from JSON file"""
    with open(filename, "r") as f:
        return (json.load(f))
