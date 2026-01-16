import os
import sys
import unittest
from typing import List, Tuple, cast

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.filter_docs.filter_sql_docs import reduce_items, remove_items_if_present


class MyTestCase(unittest.TestCase):
    def test_reduce_items(self):
        result = cast(List[int], reduce_items([1, 2, 3], [2]))
        self.assertEqual(result, [1, 3])
        result = cast(List[int], reduce_items([1, 2, 3], [1, 2, 3]))
        self.assertEqual(result, [])
        result = cast(List[int], reduce_items([1, 2, 3], [1, 2, 4, 5]))
        self.assertEqual(result, [3])
        result = cast(List[int], reduce_items([1, 2, 3], [4, 5, 6]))
        self.assertEqual(result, [1, 2, 3])
        result = cast(List[int], reduce_items([1, 2, 3], []))
        self.assertEqual(result, [1, 2, 3])
        result = cast(List[int], reduce_items([], []))
        self.assertEqual(result, [])
        result = cast(List[int], reduce_items([], [1, 2, 3]))
        self.assertEqual(result, [])

    def test_remove_items_if_present(self):
        result_items, items_were_removed = cast(
            Tuple[List[int], bool],
            remove_items_if_present([1, 2, 3], []),
        )
        self.assertEqual(result_items, [1, 2, 3])
        self.assertFalse(items_were_removed)
        result_items, items_were_removed = cast(
            Tuple[List[int], bool],
            remove_items_if_present([1, 2, 3], [2]),
        )
        self.assertEqual(result_items, [1, 3])
        self.assertTrue(items_were_removed)
        result_items, items_were_removed = cast(
            Tuple[List[int], bool],
            remove_items_if_present([1], [2]),
        )
        self.assertEqual(result_items, [1])
        self.assertFalse(items_were_removed)
        result_items, items_were_removed = cast(
            Tuple[List[int], bool],
            remove_items_if_present([], [1, 2, 3]),
        )
        self.assertEqual(result_items, [])
        self.assertFalse(items_were_removed)


if __name__ == "__main__":
    _ = unittest.main()
