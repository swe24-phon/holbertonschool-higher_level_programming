#!/usr/bin/python3
def max_integer(my_list=[]):
    """This function returns the largest integer in a list.
    If the list is empty, it returns None.
    parameter:
    my_list (list): A list of integers.
    return:
    int or None: largest integer in the list or None if the list is empty.
    """
    if not my_list:
        return None
    else:
        max_num = 0
        for current_num in my_list:
            if current_num > max_num:
                max_num = current_num
    return max_num
