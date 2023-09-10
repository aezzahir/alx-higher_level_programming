#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return
    elif n == 1:
        print("{0:d}".format(my_list[0]))
    else:
        for i in range(-1, -n - 1, -1):
            print("{0:d}".format(my_list[i]))
