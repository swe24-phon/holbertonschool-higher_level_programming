#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers in the list, in reverse order.
    
    Parameters:
    my_list (list): The list to modify

    Returns:
    None
    
    """

for i in my_list:
    print("{:d}".format(my_list[len(my_list - i)]))
