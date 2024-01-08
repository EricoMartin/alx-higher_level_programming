#!/usr/bin/python3
""" This module returns the peak of the list
"""


def find_peak(list_of_integers):
    """ This function returns the peak of the list
    """
    if (len(list_of_integers) == 0):
        return None

    else:
        peak = list_of_integers[0]
        for i in range(1, len(list_of_integers) - 1):
            if list_of_integers[i] >= peak - 1:
                peak = list_of_integers[i]
        return peak
