#!/usr/bin/python3
""" models/base.py module declaration """


class Base:
    """ base class declaration """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Constructor declaration
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
