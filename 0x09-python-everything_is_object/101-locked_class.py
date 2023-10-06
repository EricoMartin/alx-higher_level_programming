#!/usr/bin/python3
""" This the LockedClass Module """


class LockedClass:
    """ LockedClass Declaration """
    def __init__(self, first_name = None):
        """The init block"""
        if self.first_name is not None:
            self. first_name = first_name
        else:
            raise AttributeError()
