#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints the first integer in the list; if the list is empty it prints None."""
    if my_list is None:
        print(" ")
    else:
        for integer in my_list:
            print("{:d}".format(my_list[integer]))
