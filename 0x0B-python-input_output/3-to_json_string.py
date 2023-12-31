#!/usr/bin/python3


"""
This module defines a function to_json_string(my_obj)
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.
    args:
        my_obj : object to serialize
    """
    json_obj = json.dumps(my_obj)
    return json_obj
