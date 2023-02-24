#!/usr/bin/python3
"""
    Module test for rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    def test_base_create(self):
        rectangle_1 = Rectangle(1, 2)
        self.assertEqual(rectangle_1.id, 1)


if __name__ == '__main__':
    unittest.main()
