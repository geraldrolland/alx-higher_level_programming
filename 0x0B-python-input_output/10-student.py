#!/usr/bin/python3


"""
This module defines the class Student
"""


class Student:

    """Define class student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the attribute of the object.
        args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        my_dict_copy = self.__dict__.copy()
        key_list = my_dict_copy.keys()
        for key in attrs:
            if key in key_list:
                value = my_dict_copy[key]
                new_dict.update({key: value})
            continue
        return new_dict
