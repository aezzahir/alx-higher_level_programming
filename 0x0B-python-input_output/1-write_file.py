#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """ This is a function that write text to a file """
    with open(filename, 'w', encoding="utf-8") as f:
        f.read(text)
