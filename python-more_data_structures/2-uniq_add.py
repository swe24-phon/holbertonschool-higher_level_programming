#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add elements to a set of unique integers.
    parameters:
    my_list (list): A list of integers.
    return:
    sum: total sum of unique integer
    """
    sum = 0
    set_list = {my_list}
    for i in set_list:
        sum += set_list[i]
    return sum
