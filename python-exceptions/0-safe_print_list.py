#!/usr/bin/python3
def i_count(lst):
    """
    This function counts the number of elements in a list.
    parameters:
    lst (list): The list to be counted
    return:
    int: The number of elements in the list
    """
    count = 0
    for _ in lst:
        count += 1
    return count


def safe_print_list(my_list=[], x=0):
    """
    This function prints a list of elements, but only if the list\
        is not empty.
    parameters:
    my_list (list): The list to be printed
    x (int): The minimum number of elements required in the list\
        to print it
    return:
    int: The number of elements printed
    """

    try:
        count = 0
        for i in range(min(x, i_count(my_list))):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        return count
    