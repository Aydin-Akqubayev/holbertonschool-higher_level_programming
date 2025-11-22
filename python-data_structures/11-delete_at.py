#!/usr/bin/python3
def delete_at(my_list, idx):
    for i in range(len(my_list)):
        if i == idx:
            my_list.remove(my_list[i])
    return my_list
