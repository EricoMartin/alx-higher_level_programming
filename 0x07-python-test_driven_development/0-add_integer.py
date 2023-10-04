#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """ This is the add_integer function Declaration

        Args:
            a: a number or float
            b: another number or float

        Returns:
            integer addition
    """

    var_a = isinstance(a, int) or isinstance(a, float)
    var_b = isinstance(b, int) or isinstance(b, float)

    if not var_a:
        raise TypeError("a must be an integer")
    elif not var_b:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
