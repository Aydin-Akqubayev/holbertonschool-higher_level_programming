#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(sorted(a_dictionary.items()))
    keys = (a_dictionary.keys())
    values = a_dictionary.values()
    for key, value in zip(keys, values):
        print("{}: {}".format(key, value))
    return a_dictionary
