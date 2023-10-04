#!/usr/bin/python3
""" This the module Declarartion"""


def add_integer(a, b=98):
    """ This is the function Declaration"""

    var_a = isinstance(a, int) or isinstance(a, float)
    var_b = isinstance(b, int) or isinstance(b, float)

    if var_a and var_b:
        if isinstance(b, float) or isinstance(a, float):
            int(a)
            int(b)
        return a + b
    elif not var_a:
        raise TypeError("a must be an integer")
    else:
        raise TypeError("b must be an integer")
