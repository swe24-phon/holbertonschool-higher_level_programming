#!/usr/bin/python3
def multiple_returns(sentence):
    """
    This function takes a sentence as input and returns a tuple\
          containing the number of vowels and consonants
    in the sentence.

    parameter:
    sentence (str): The input sentence.
    return:
    len(sentence): sentence length
    sentence[0]: First character
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
