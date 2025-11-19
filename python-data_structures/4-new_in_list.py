#!/usr/bin/python3
def new_in_list(my_list, idx, new_element):
    if idx >= 0 and idx < len(my_list):
        answer = my_list[:idx] + [new_element] + my_list[idx + 1:]
    else:
        answer = my_list
    return answer
