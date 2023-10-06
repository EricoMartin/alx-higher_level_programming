#!/usr/bin/python3
"""This is the 101-locked_class Module

    This module optimizes memory by creating obj based on 
    certain criteria.
"""


class LockedClass:
    """ LockedClass Declaration """
    __slots__ = (first_name)

    def __init__(self, first_name=None):
        """The init block"""
        if self.first_name is not None:
            self.first_name = first_name
