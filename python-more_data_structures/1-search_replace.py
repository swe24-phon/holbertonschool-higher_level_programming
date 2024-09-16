#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replace all occurrences of search with replace in my_list.
    parameters:
    my_list: The list to be modified.
    search: The value to be replaced.
    replace: The value to replace with.
    returns:
    A new list with all occurrences of search replaced with replace.
    """
    return [replace if item == search else item for item in my_list]
