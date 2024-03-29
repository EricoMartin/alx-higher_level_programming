#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """
        This is the add_integer function Declaration

        Args:
            a: a number or float
            b: another number or float

        Returns:
            integer addition
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
