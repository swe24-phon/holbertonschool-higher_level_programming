#!/usr/bin/python3
"""
write to file and print out its length
"""


def write_file(filename=""):
    """ write the file and print out its length """

    with open(filename, 'w', encoding='utf-8') as file:
        return len(file.write())
