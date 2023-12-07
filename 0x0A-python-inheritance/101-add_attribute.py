#!/usr/bin/python3
"""Define the function add_attribute(...)"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
    - obj: The object to which the attribute should be added.
    - attr_name: The name of the new attribute.
    - attr_value: The value of the new attribute.

    Raises:
    - TypeError: If the object doesn't support adding new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
