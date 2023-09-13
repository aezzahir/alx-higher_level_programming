#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for i in a_dictionary.keys():
        new_dict[i] = 2 * a_dictionary[i]
    return (new_dict)
