#!/usr/bin/python3


"""
This module defines the function save_to_json_file(my_obj, filename)
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation.
    args:
        my_obj: jason object
        filename: name of file
    """
    with open(filename, "w", encoding="UTF8") as file:
        json.dump(my_obj, file)
