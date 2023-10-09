#!/usr/bin/python3
"""This module contains the class MyList that inherits from list"""

class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
