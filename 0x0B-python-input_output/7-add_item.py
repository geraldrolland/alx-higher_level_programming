#!/usr/bin/python3


"""
This module provide a programme
"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    file = load_from_json_file("add_item.json")
except FileNotFoundError:
    save_to_json_file([], "add_item.json")
finally:
    file = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        i = 1
        while i < len(sys.argv):
            file.append(sys.argv[i])
            i += 1
        save_to_json_file(file, "add_item.json")
