#!/usr/bin/python3
""" This the module Declarartion"""


def add_integer(a, b=98):
    """ This is the function Declaration"""

    var_a = isinstance(a, int) or isinstance(a, float)
    var_b = isinstance(b, int) or isinstance(b, float)

    if var_a and var_b:
        return int(a) + int(b)
    elif not var_a:
        raise TypeError("a must be an integer")
    elif not var_b:
        raise TypeError("b must be an integer")
