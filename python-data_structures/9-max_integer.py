#!/usr/bin/python3
def compare(a, b):
    if a < b:
        res = b
    else:
        res = a
    return res


def max_integer(my_list):
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if i == 0:
            a = my_list[i]-1
        a = compare(a, my_list[i])
    return a
