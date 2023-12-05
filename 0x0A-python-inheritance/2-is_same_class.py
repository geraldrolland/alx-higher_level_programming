#!/usr/bin/python3


"""
This module 2-is_same_class defines a function is_same_class(...)
"""


def is_same_class(obj, a_class):
    """returns True if the object belong to the specified class.
    args:
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class):
        return True
    return False
