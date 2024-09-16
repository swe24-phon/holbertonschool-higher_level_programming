#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    new dictionary * 2
    parameters:
    a_dictionary (dict): The dictionary to multiply by 2
    return:
    dict: A new dictionary with all values multiplied by 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    return new_dict
