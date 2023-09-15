#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    item = []
    for key, key_value in a_dictionary.items():
        if key_value is value:
            item.append(key)
    for x in item:
        del a_dictionary[x]
    return a_dictionary
