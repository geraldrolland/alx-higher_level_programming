#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum_elem = 0
    div = 0
    for elem in my_list:
        result = elem[0] * elem[1]
        div += elem[1]
        sum_elem += result
    return sum_elem / div
