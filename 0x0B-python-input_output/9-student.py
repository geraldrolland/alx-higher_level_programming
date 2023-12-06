#!/usr/bin/python3


"""
This module defines the class Student
"""


import json


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialize the attribute of the object.
        args:
            first_name : first name
            last_name : last name
            age : age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary"""
        return json.dumps(self.__dict__)
