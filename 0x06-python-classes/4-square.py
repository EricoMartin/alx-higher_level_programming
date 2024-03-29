#!/usr/bin/python3
"""This is the sqaure module"""


class Square:
    """This class defines a sqaure instance"""

    def __init__(self, size=0) -> None:
        """This method instantiates the sqaure object

        Args:
            size (int): Size of the sqaure
        """

        self.__size = size

    @property
    def size(self):
        """ This is a getter property for size attribute of Square class
        Args:
            self

        Returns:
            int: The size of a square instance.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This is a value setter property for size attribute of Square class
        Args:
            self (Square): An instance of this object
            value (int): Integer value to set the sqaure size

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """This describes an Area of a square

        Returns:
            int: The area of a square instance.
        """
        return self.__size ** 2
