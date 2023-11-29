#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """Print the first name and last name"""
    if type(first_name) not in [str] or \
            first_name is None or first_name == "":
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str) or last_name is None:
        raise TypeError("last_name must be a string")
    for char in first_name:
        if char.isdigit() is True:
            raise TypeError("first_name must be a string")
        continue
    if last_name == "":
        print("My name is {}".format(first_name))
        return
    for char in last_name:
        if char.isdigit() is True:
            raise TypeError("last_name must be a string")
        continue
    print("My name is {} {}".format(first_name, last_name))
