#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers in the list, in reverse order.

    Parameters:
    my_list (list): The list to modify

    Returns:
    None
    """
    if my_list is None:
        my_list = []
    for elem in my_list[::-1]:
        print("{:d}".format(elem))
