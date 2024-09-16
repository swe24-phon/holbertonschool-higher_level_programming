#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add elements to a set of unique integers.
    parameters:
    my_list (list): A list of integers.
    return:
    sum: total sum of unique integer
    """
    if my_list is None:
        my_list = []
    unique_sum = sum(set(my_list))
    return unique_sum
