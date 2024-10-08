#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides a by b and prints the result, handling potential\
        division by zero errors.
    parameters:
    a (int): The dividend.
    b (int): The divisor.
    return:
    result:  The result of the division.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
