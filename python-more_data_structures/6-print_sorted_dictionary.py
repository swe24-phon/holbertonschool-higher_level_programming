#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    parameters:
    a_dictionary (dict): The dictionary to be printed.
    return:
    None
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
