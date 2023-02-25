"""
    Module test for rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    rectangle_1 = Rectangle(1, 2)

    def test_rectangle_create(self):
        self.assertEqual(self.rectangle_1.width, 1)

    def test_rectangle_create_except_1(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "2")

    def test_rectangle_create_except_2(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "2")

    def test_rectangle_create_except_3(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")

    def test_rectangle_create_except_4(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")


if __name__ == '__main__':
    unittest.main()