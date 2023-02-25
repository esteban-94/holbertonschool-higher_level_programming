"""
    Module test for rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    rectangle_1 = Rectangle(1, 2)

    def test_rectangle_create_1(self):
        self.assertEqual(self.rectangle_1.width, 1)

    def test_rectangle_create_except_1(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 2)

    def test_rectangle_create_except_2(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "2")

    def test_rectangle_create_except_3(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")

    def test_rectangle_create_except_4(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")

    def test_rectangle_create_2(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.id, 5)

    def test_rectangle_create_except_5(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-1, 2)

    def test_rectangle_create_except_6(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, -2)

    def test_rectangle_create_except_7(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 2)

    def test_rectangle_create_except_8(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 0)

    def test_rectangle_create_except_9(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -1)

    def test_rectangle_create_except_10(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -1)


if __name__ == '__main__':
    unittest.main()