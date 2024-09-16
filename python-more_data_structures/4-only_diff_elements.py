#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    This function takes two sets as input and returns a new set\
         containing only the elements that are present in either set_1 or\
            set_2, 1 but not in set_2, and vice versa.
    parameters:
    set_1 (set): The first set.
    set_2 (set): The second set.
    returns:
    set: A new set containing elements that are in set_1 but not in set_2

    """
    return set_1.symmetric_difference(set_2)
