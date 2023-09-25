#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for i in my_list:
        try:
            num++
            print(i)
        except Exception as exc:
            print(type(exc))
    return num
