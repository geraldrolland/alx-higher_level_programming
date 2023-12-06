#!/usr/bin/python3


"""
This module defines a function from_json_string(my_str)
"""


import json


def from_json_string(my_str):
    """ returns an object  represented by a JSON string.
    args:
        my_str: jason object
    """
    return json.loads(my_str)
