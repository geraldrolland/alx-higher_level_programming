#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    for elem in my_list:
        if elem == my_list[idx]:
            my_list[idx] = element
            return my_list
            break
        continue
