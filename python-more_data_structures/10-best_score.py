#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the best score if it exists in the dictionary, otherwise None
    parameters:
    a_dictionary (dict): The dictionary to be printed.
    return:
    None
    """
    if a_dictionary is None:
        return None
    elif not a_dictionary:
        return None
    else:
        best_score = none
        for key in a_dictionary:
            if best_score < a_dictionary[key]:
                best_score = a_dictionary[key]
    return best_score
    