#!/usr/bin/python3

"""
This module defines a funntion
"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None
    if len(list_of_integers) > 2:
        peak_list = []
        i = 1
        j = -1
        index = 0
        peak = list_of_integers[0]
        while i < len(list_of_integers):
            if peak >= list_of_integers[i] and index == 0:
                peak_list.append(peak)
            j += 1
            index += 1
            i += 1
            peak = list_of_integers[index]
            if i < len(list_of_integers):
                if peak >= list_of_integers[i] and peak >= list_of_integers[j]:
                    peak_list.append(peak)
        if len(peak_list) == 1:
            return peak_list[0]
        elif len(peak_list) == 2:
            return max(peak_list[0], peak_list[1])
        else:
            i = 0
            max_num = peak_list[0]
            while i < len(peak_list):
                if max_num < peak_list[i]:
                    max_num = peak_list[i]
                i += 1
            return max_num
