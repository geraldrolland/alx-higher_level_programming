#!/usr/bin/python3


"""
This module 0-lookup defines a function lookup(...)
"""


def lookup(obj):
    """Return the list of attribute and method of an object.
    args:
        obj: object of a class
    """
    return dir(obj)
