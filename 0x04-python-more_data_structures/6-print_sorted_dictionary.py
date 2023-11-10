#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == {}:
        return
    only_key = a_dictionary.keys()
    only_key = sorted(only_key)
    for key in only_key:
        print("{}: {}".format(key, a_dictionary[key]))
