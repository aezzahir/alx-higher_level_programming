#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0 or idx >= n:
        return my_list
    else:
        copy = my_list.copy()
        copy[idx] = element
        return copy
