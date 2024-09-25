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
    for i, char in enumerate(text):
        print(char, end='')
        if char in ['.', '?', ':']:
            print('\n', end='')
            if i < len(text) - 1 and text[i+1] == ' ':
                next(iter(text[i+1:]), '')
        