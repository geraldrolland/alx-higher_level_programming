#!/usr/bin/python3


"""
This module defines the class Student
"""


import json


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
            my_str = json.dumps(self.__dict__)
            return (json.loads(my_str))
        my_str = json.dumps(self.__dict__)
        my_dict = json.loads(my_str)
        new_dict = {}
        my_dict_copy = my_dict.copy()
        key_list = my_dict.keys()
        for key in attrs:
            if key in key_list:
                value = my_dict_copy[key]
                new_dict.update({key: value})
            continue
        return new_dict
