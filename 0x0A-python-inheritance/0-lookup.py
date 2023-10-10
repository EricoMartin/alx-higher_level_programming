#!/usr/bin/python3
""" lookup(obj): A module that conatins the a function that
    returns the list of available attributes and methods of
    an object.
"""

def lookup(obj):
    return (dir(obj))
