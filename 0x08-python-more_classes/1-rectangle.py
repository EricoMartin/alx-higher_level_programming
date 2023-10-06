#!/usr/bin/python3
"""
Define an empty class Rectangle
"""


class Rectangle:
    """
        A Rectangle class

        Args:
            width: An integer
            height: Another integer

        Returns:
            None

    """
    def __init__(self, width=0, height=0):
        """ The initialization method """
        
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width getter property """

        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method """

        if type(width) is int:
            self.__width = value
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ height getter property """

        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """

        if type(height) is int:
            self.__height = value
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
