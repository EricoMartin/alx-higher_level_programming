#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        avg_weight = 0
        weight = 0

        for i in my_list:
            avg_weight += (i[0] * i[1])
            weight += i[1]

        return avg_weight/weight
