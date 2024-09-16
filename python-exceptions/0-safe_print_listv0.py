#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    This function prints a list of elements, but only if the list\
        is not empty.
    If the list is empty, it prints a message indicating that the\
        list is empty.
    The function also takes an optional argument x, which is used\
        to print a message
    if the list is not empty, but the number of elements in the\
        list is less than x
    parameters:
    my_list (list): The list to be printed
    x (int): The minimum number of elements required in the list\
        to print it
    return:
    None
    """
    def length(my_list):
        for i in my_list:
            l = i+1
            return l
    if not my_list:
        print("The list is empty.")
        elif length(my_list) < x:
print(f"The list is not empty, but it has only {length(my_list)} elements.")
else:
print(my_list)
