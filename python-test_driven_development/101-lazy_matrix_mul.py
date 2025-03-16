#!/usr/bin/python3
"""
This module defines a function that multiplies two matrices using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using the module NumPy

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Returns:
        str: result of the multiplication
    Raises:
        ValueError: if scalar operands are used
    """
    try:
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)
        result = np.matmul(a, b)
        return str(result)
    except ValueError:
        raise ValueError("Scalar operands are not allowed, use '*' instead")