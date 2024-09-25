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
    sentences = text.split('?')
    new_text = ''
    for sentence in sentences:
        subsentences = sentence.split('.')
        for subsentence in subsentences:
            subsentence = subsentence.strip()
            if subsentence:
                new_text += subsentence + '.\n\n'
        new_text = new_text.rstrip('\n')
        new_text += '?\n\n'
    sentences = new_text.split(':')
    new_text = ''
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            new_text += sentence + ':\n\n'
    print(new_text.rstrip())
        