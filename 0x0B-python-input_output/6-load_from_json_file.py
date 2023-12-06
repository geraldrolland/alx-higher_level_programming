#!/usr/bin/python3


"""
This module defines the function load_from_json_file(filename)
"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”.
    args:
        filename: name of file
    """
    with open(filename, "r", encoding="UTF8") as file:
        return json.load(file)
