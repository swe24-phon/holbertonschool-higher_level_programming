#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the best score if it exists in the dictionary,\
        otherwise returns None.
    Parameters:
    a_dictionary (dict): The dictionary to be printed.
    Returns:
    The key with the best score in the dictionary, or None if the\
        dictionary is empty.
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        best_score = None
        best_key = None
        for key, value in a_dictionary.items():
            if best_score is None or value > best_score:
                best_score = value
                best_key = key
        return best_key
