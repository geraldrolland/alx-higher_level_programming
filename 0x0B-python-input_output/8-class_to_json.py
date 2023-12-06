

"""
This module define function class_to_json(...)
"""


import json


def class_to_json(obj):
    """convert class object to jason"""
    my_str = json.dumps(obj.__dict__)
    return json.loads(my_str)
