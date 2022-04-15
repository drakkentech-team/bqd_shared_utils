import unittest
from src.filter_docs.filter_sql_docs import *


class MyTestCase(unittest.TestCase):
    def test_reduce_items(self):
        result = reduce_items([1, 2, 3], [2])
        self.assertEqual(result, [1, 3])
        result = reduce_items([1, 2, 3], [1, 2, 3])
        self.assertEqual(result, [])
        result = reduce_items([1, 2, 3], [1, 2, 4, 5])
        self.assertEqual(result, [3])
        result = reduce_items([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3])
        result = reduce_items([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])
        result = reduce_items([], [])
        self.assertEqual(result, [])
        result = reduce_items([], [1, 2, 3])
        self.assertEqual(result, [])

    
    def test_remove_items_if_present(self):
        result_items, items_were_removed = remove_items_if_present([1, 2, 3], [])
        self.assertEqual(result_items, [1, 2, 3])
        self.assertFalse(items_were_removed)
        result_items, items_were_removed = remove_items_if_present([1, 2, 3], [2])
        self.assertEqual(result_items, [1, 3])
        self.assertTrue(items_were_removed)
        result_items, items_were_removed = remove_items_if_present([1], [2])
        self.assertEqual(result_items, [1])
        self.assertFalse(items_were_removed)
        result_items, items_were_removed = remove_items_if_present([], [1, 2, 3])
        self.assertEqual(result_items, [])
        self.assertFalse(items_were_removed)


if __name__ == "__main__":
    unittest.main()
