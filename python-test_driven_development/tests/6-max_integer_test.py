#!/usr/bin/python3
"""Unittest for max_integer([])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements_list(self):
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_list_with_negative_numbers(self):
        self.assertEqual(max_integer([-3, -1, -4, -2]), -1)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([3, 3, 4, 2]), 4)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            max_integer([3, 'a', 4, 2])

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

if __name__ == '__main__':
    unittest.main()
