"""
    Module test for rectangle class
"""


import unittest
import io
import unittest.mock
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""

    """ Testing width conditions """
    def test_width(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)


if __name__ == '__main__':
    unittest.main()