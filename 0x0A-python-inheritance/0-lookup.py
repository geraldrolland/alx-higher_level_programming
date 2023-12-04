#!/usr/bin/python3


"""
This module 0-lookup defines a function lookup(...)
"""


def lookup(obj):
    """Return the list of attribute and method of an object.
    args:
        obj: object of a class
    """
    my_list = []
    my_dict = obj.__dict__
    keys = my_dict.keys()
    for key in keys:
        my_list.append(key)
    return my_list
