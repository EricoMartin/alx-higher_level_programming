#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """A Rectangle class"""

    def __init__(self, width=0, height=0):
        """ The initialization method """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter property """

        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter property """

        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
