#!/usr/bin/python3

def magic_string(my_list=[]):
    my_list += ["BestSchool"]
    return (', '.join([str(sch) for sch in my_list]))
