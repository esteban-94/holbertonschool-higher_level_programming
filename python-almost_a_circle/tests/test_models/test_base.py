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
    base_89 = Base(89)

    def test_base_create(self):
        self.assertEqual(self.base_1._Base__nb_objects, 2)
        self.assertEqual(self.base_1.id, 1)

    def test_base_update_id(self):
        self.assertEqual(self.base_2._Base__nb_objects, 2)
        self.assertEqual(self.base_2.id, 2)

    def test_base_id(self):
        self.assertEqual(self.base_89._Base__nb_objects, 2)
        self.assertEqual(self.base_89.id, 89)

    def test_base_to_json_string_void(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_base_to_json_string_full(self):
        self.assertEqual(Base.to_json_string([{'id':12}]), '[{"id": 12}]')

    def test_base_from_json_string_void(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_base_from_json_string_full(self):
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
