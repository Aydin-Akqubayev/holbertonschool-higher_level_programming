#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < len(my_list) and idx >= 0:
        my_list[idx] = new_element
    return my_list
