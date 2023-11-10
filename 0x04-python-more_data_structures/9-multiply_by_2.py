#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dict = {}
    key_list = a_dictionary.keys()
    for key in key_list:
        value = a_dictionary[key] * 2
        my_dict.update({key: value})
    return my_dict
