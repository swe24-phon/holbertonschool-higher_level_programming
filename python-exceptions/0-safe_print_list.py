#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    This function prints a list of elements, but only if the list\
        is not empty.
    parameters:
    my_list (list): The list to be printed
    x (int): The minimum number of elements required in the list\
        to print it
    return:
    None
    """

    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except:
        return count
