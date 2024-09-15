#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    This function adds two tuples together.

    parameter:
    tuple_a (tuple): The first tuple to be added.
    tuple_b (tuple): The second tuple to be added.
    Return:
    A tuple with 2 integers
    """

    sum1 = 0
    sum2 = 0

    if len(tuple_a) > 0:
        sum1 += tuple_a[0]
    if len(tuple_b) > 0:
        sum1 += tuple_b[0]

    if len(tuple_a) > 1:
        sum2 += tuple_a[1]
    if len(tuple_b) > 1:
        sum2 += tuple_b[1]
    return sum1, sum2
