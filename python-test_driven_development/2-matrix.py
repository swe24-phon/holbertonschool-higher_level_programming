def divide_matrix(matrix, divisor):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix.
        divisor (float): The value to divide the matrix elements by.

    Returns:
        list of lists: The resulting matrix with all elements divided by the divisor.
    """
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element / divisor)
        result.append(new_row)
    return result