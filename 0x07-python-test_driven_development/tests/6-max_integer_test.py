#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """this class for testing max_integer function"""
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

    def test_large_negative_list(self):
        self.assertEqual(max_integer(list(range(-10000, 0))), -1)


if __name__ == '__main__':
    unittest.main()
