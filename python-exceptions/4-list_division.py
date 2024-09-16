#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides two lists element by element.
    parameters:
    my_list_1 (list): The first list of numbers.
    my_list_2 (list): The second list of numbers.
    list_length (int): The length of the lists.
    Returns:
    list: A list of the division results.
    """
    result = []
    for i in range(list_length):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            division by 0
        except TypeError:
            print("wrong type")
        finally:
            return result
        
