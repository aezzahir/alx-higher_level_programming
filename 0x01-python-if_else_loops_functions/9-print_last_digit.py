#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = (-1 * number) % 10
    print("{}".format(last_digit), end='')
    return last_digit
