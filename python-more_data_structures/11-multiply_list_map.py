#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    Multiply each element in a list by a given number.
    parameters:
    my_list: list of elements
    number: multiplier
    returns:
    new_list: list of elements multiplied by the number
    """
    return list(map(lambda x: x * number, my_list))
