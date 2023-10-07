#!/usr/bin/python3
"""this module is for printing a text"""


def text_indentation(text):
    """function to add two lines after ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_to_newline = [".", "?", ":"]
    result = []

    for char in text:
        result.append(char)
        if char in punctuation_to_newline:
            result.append('\n')
            result.append('\n')

    lines = ''.join(result).splitlines()
    for line in lines:
        print(line.strip())


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
