#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key from a dictionary.
    parameters:
    a_dictionary (dict): The dictionary to delete from.
    key (str): The key to delete. Defaults to an empty string.
    return:
    dict: The dictionary with the key deleted.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
