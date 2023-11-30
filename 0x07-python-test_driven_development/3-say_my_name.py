#!/usr/bin/python3


"""
This is module docstring for 3-say_my_name

This module provide the function say_my_name(..)
"""


def say_my_name(first_name, last_name=""):
    """Print the first name and last name.
    args:
        first_name(str): first name
        last_name(str): last name
    """
    if type(first_name) not in [str] or \
            first_name is None or first_name == "":
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    for char in first_name:
        if char.isdigit() is True:
            raise TypeError("first_name must be a string")
        continue
    for char in last_name:
        if char.isdigit() is True:
            raise TypeError("last_name must be a string")
        continue
    print("My name is {} {}".format(first_name, last_name))
