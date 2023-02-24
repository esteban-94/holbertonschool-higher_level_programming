#!/usr/bin/python3
"""
    Module test for base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""
    base_1 = Base()
    base_2 = Base()
    base_4 = Base(4)

    def test_base_create(self):
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_1._Base__nb_objects, 1)

if __name__ == '__main__':
    unittest.main()
