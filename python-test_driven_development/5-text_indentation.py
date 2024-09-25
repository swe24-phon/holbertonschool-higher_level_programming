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
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n\n", end="")
            if i + 1 < len(text) and text[i + 1] == " ":
                print(end="")
                i += 1
        i += 1
        