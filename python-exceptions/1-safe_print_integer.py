#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format() and returns True if\
        successful.
    
    Args:
        value (any): The value to be printed as an integer.
    
    Returns:
        bool: True if value is an integer and printed successfully,\
            False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
