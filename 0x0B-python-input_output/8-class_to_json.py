

"""
This module define function class_to_json(...)
"""


import json


def class_to_json(obj):
    """convert class object to jason"""
    return json.dumps(obj.__dict__)
