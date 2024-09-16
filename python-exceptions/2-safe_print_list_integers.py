#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a given list of integers.
    The function should be safe by avoiding any TypeError.
    parameters:
    my_list (list): The list of integers to print.
    x (int): The number of elements to print.
    Returns:
    int: The number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return count
