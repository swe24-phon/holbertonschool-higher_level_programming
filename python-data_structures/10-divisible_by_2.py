#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Returns a list of all integers in the input list that are divisible\
          by 2.
    parameter:
    my_list (list): A list of integers.
    return:
    list: A list of integers that are divisible by 2.

    """
    return [i % 2 == 0 for i in my_list]
