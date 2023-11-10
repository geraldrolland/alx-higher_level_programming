#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_0 = set_1.difference(set_2)
    set_01 = set_2.difference(set_1)
    set_0.update(set_01)
    return set_0
