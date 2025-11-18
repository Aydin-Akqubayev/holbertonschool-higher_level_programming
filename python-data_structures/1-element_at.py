#!/usr/bin/python3
def element_at(my_list, idx):

    try:
        if idx >= 0:
            return my_list[idx]

        else:
            return None

    except IndexError:
        return None 
