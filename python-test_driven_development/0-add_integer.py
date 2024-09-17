#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function will add two integer or float
    Otherwise raise a TypeError for given incorrect argument type.
    parameters:
    a (int): first integer
    b (int): second integer
    return:
    int: sum of a and b
    Raises:
    TypeError: If a or b aren't integer and/or float numbers
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)    
    return a + b
