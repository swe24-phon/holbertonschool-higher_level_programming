#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete the element at the specified position in a list.
    parameters:
    my_list (list): The list to delete from.
    idx (int): The index of the element to delete.
    return:
    list: The updated list.    
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        del my_list[idx]
        return my_list
