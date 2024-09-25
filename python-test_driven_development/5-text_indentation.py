#!/usr/bin/python3
"""
This module is composed by a function that 
prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """
    prints 2 new lines after ".?:" characters

    Parameters:
        text: string

    Returns: None
    Raises:
        TypeError: if text is not a string

    """
    for char in text:
        print(char, end='')
        if char in ['.', '?', ':']:
            print('\n\n', end='')
        