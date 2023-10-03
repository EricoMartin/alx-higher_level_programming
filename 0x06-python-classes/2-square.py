#!/usr/bin/python3
"""This is the sqaure module"""


class Square:
    """This class defines a sqaure instance"""

    def __init__(self, size=0):
        """This method instantiates the sqaure object"""

        if isinstance(int, size):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
