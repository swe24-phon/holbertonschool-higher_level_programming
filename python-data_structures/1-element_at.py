#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specified index.

    Parameters:
    my_list (list): The list from which an element is to be retrieved.
    idx (int): The index of the element to retrieve.

    Returns:
    The element at the specified index if the index is valid.
    None if the index is negative or greater than the length of the list.
    """
    if idx < 0:
        return (None)
    elif idx > len(my_list) - 1:
        return (None)
    else:
        return (my_list[idx])
