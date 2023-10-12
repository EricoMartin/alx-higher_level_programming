#!/usr/bin/python3
""" append_after module declaration
"""


def append_after(filename="", search_string="", new_string=""):
    """

    """

    with open(filename, "a") as f:
        for line in f:
            if line.find(search_string) != -1:
                f.write(new_string)
