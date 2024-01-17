#!/usr/bin/python3


"""
This module defines the class Base
"""


import json


class Base:
    """Defines a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the attribute of the object.
        args:
            id(int): value of the object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            return
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        if type(list_objs) is not list or None:
            file_json = "{}.json".format(cls.__name__)
            with open(file_json, "w", encoding="UTF8") as file:
                file.write("[]")
                return
        my_list = []
        for elem in list_objs:
            my_list.append(elem.to_dictionary())
        obj_str = cls.to_json_string(my_list)
        class_name = cls.__name__
        file_json = "{}.json".format(class_name)
        with open(file_json, "w", encoding="UTF8") as my_file:
            my_file.write(obj_str)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        if type(list_objs) is not list or None:
            file_csv = "{}.csv".format(cls.__name__)
            with open(file_csv, "w", encoding="UTF8") as file:
                file.write("[]")
                return
        my_list = []
        for elem in list_objs:
            my_list.append(elem.to_dictionary())
        obj_str = cls.to_json_string(my_list)
        class_name = cls.__name__
        file_csv = "{}.csv".format(class_name)
        with open(file_csv, "w", encoding="UTF8") as my_file:
            my_file.write(obj_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(1, 1)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        my_list_obj = []
        if cls.__name__ == "Rectangle":
            try:
                with open("Rectangle.json", "r", encoding="UTF8") as file:
                    obj_str = file.read()
                    list_obj = cls.from_json_string(obj_str)
                    for elem in list_obj:
                        obj = cls.create(**elem)
                        my_list_obj.append(obj)
                    return my_list_obj
            except FileNotFoundError:
                return []
        else:
            try:
                with open("Square.json", "r", encoding="UTF8") as file:
                    obj_str = file.read()
                    list_obj = cls.from_json_string(obj_str)
                    for elem in list_obj:
                        obj = cls.create(**elem)
                        my_list_obj.append(obj)
                    return my_list_obj
            except FileNotFoundError:
                return []

    @classmethod
    def load_from_file_csv(cls):
        """returns a list of instances"""
        my_list_obj = []
        if cls.__name__ == "Rectangle":
            try:
                with open("Rectangle.csv", "r", encoding="UTF8") as file:
                    obj_str = file.read()
                    list_obj = cls.from_json_string(obj_str)
                    for elem in list_obj:
                        obj = cls.create(**elem)
                        my_list_obj.append(obj)
                    return my_list_obj
            except FileNotFoundError:
                return []
        else:
            try:
                with open("Square.csv", "r", encoding="UTF8") as file:
                    obj_str = file.read()
                    list_obj = cls.from_json_string(obj_str)
                    for elem in list_obj:
                        obj = cls.create(**elem)
                        my_list_obj.append(obj)
                    return my_list_obj
            except FileNotFoundError:
                return []
