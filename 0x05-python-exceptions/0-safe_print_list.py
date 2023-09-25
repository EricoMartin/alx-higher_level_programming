#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            num++
            print(my_list[i], end="")
        except IndexError as exc:
            print(type(exc))
            break
        finally:
            print()
    return num
