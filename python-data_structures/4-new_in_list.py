
#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Insert a new element at a specific index in a list.

    parameter:
    my_list (list): The list to be modified.
    idx (int): The index at which the new element will be inserted.
    element (any): The new element to be inserted.

    Returns:
    list: The modified list.    
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list.insert(idx, element)
    return my_list
