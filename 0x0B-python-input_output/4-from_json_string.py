#!/usr/bin/python3
"""JSON to object module"""
import json


def from_json_string(my_str):
    """from  json string to object string"""
    return (json.loads(my_str))
