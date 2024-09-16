#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary with a new key-value pair.
    parameters:
    a_dictionary (dict): The dictionary to be printed.
    key (any): The key to be added to the dictionary.
    value (any): The value associated with the key.
    Returns:
    dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
