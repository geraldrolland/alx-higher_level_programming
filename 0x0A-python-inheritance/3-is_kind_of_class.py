#!/usr/bin/python3


"""
This module 3-is_kind_of_class defines a is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """return true if the object is an instance of a class
    args:
        obj: object
        a_class: class
    """
    if isinstance(obj, a_class):
        return True
    return False
