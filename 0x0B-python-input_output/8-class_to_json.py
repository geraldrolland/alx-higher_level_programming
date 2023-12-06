#!/usr/bin/python3


"""
This module define function class_to_json(...)
"""


def class_to_json(obj):
    """convert class object to jason"""
    return obj.__dict__
