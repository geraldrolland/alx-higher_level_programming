#!/usr/bin/python3


"""
This module 4-inherits_from define inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """ returns True if the object belong to a class that inherited
    args:
        obj: object
        a_class: class
    """
    if type(obj) is a_class:
        return False
    elif issubclass(type(obj), a_class):
        return True
    return False
