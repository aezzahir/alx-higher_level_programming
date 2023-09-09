#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return
    for i in my_list[-1:-n-1:-1]:
        print("{:d}".format(i))
