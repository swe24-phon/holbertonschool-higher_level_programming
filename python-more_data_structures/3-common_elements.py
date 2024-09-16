#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Return a set of elements common to both input sets.
    parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.
    returns:
    set: A set of elements common to both input sets.
    """
    return set_1.intersection(set_2)
