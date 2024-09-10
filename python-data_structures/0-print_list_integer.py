#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints the first integer in the list; if the list is empty it prints None."""
    if len(my_list) == 0:
        print(None)
    else:
        for i in range(len(my_list)):
            print("{}".format(my_list[i]))
