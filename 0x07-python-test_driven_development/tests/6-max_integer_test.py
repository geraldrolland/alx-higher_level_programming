#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):

        """Test for maximum integer in a list"""

        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_single_elem(self):

        """Test for single element in list"""

        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):

        """Test empty list"""

        self.assertEqual(max_integer([]), None)

    def test_same_list_elem(self):

        """Test for the same element in a list"""

        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_neg_float_elem(self):

        """Test for negative list of flaot type"""

        self.assertEqual(max_integer([-1, -10, -4]), -1)

    def test_string(self):
        """Function test string argument"""
        self.assertEqual(max_integer("hey"), "y")

    def test_float(self):

        """Function test float argument"""

        self.assertEqual(max_integer([2.4, 0.5, 4.5]), 4.5)

    def test_list_string(self):

        """test list containing string types"""

        self.assertEqual(max_integer(["cherry", "pawpaw", "orange"]), "pawpaw")

    def test_for_none(self):

        """test if the list is None"""

        self.assertEqual(max_integer([None]), None)

    def test_empty_str(self):

        """Test for empty string"""

        self.assertEqual(max_integer(""), None)
