#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return "None"
    value_list = a_dictionary.values()
    for value in value_list:
        for elem in value_list:
            if value == elem:
                continue
            elif value < elem:
                value = elem
            continue
        key_list = a_dictionary.keys()
        for key in key_list:
            if value == a_dictionary[key]:
                return key
            continue
