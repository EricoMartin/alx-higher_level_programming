#!/usr/bin/python3
""" 8-rectangle module """


BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle - a class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ The init method

            Args:
                width: private width attribute
                height: private height attribute

            Returns:
                None
        """
        integer_validator("width", width)
        integer_validator("height", height)
        self.__width = width
        self.__height = height