#!/usr/bin/python3


"""
This module define function class_to_json(...)
"""


def class_to_json(obj):
    """convert class object to jason"""
    my_str = json.dumps(obj.__dict__)
    return json.loads(my_str)
