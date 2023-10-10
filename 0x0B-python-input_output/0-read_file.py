#!/usr/bin/python3
""" This is a function that reads a text file (UTF8) and prints it to
    stdout"""


def read_file(filename=""):
    """ This is a function that read a file """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
