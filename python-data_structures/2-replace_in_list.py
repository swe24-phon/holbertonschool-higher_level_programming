#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replace the element at the specified index in the list.

    Parameters:
    my_list (list): The list to modify
    idx (int): The index at which to replace the element
    element: The new element to insert

    Returns:
    list: The modified list if the index is within range,
    otherwise the original list
    """

    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
