#!/usr/bin/python3
""" 3-to_json_string.py Module Declaration """


def to_json_string(my_obj):
    """ to_json_string - retuens the json representattion of an obj.

        Args:
            my_obj: the object to be serialized

        Returns:
            json representation of an object
    """
    import json;
    json.dumps(my_obj
