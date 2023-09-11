#!/usr/bin/python3
def print_list_integer(my_list=[]):
    res1 = 0
    while res1 < len(my_list):
        print("{:d}".format(my_list[res1]))
        res1 += 1
