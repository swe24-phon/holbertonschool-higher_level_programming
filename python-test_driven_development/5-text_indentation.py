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
    sentences = text.split(". ")
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.endswith((":?", "?", ".")):
            sentence = sentence.rstrip("?:")
            print(sentence + ":", end="")
        else:
            print(sentence, end="")
        print("\n\n", end="")
        