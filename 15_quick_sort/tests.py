import unittest

from quick_sort import quickSort


class TestQuickSort(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        quickSort(arr)
        self.assertEqual(arr, [])

    def test_single_element(self):
        arr = [5]
        quickSort(arr)
        self.assertEqual(arr, [5])

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        quickSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        quickSort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        quickSort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_duplicates(self):
        arr = [2, 2, 2, 2, 2]
        quickSort(arr)
        self.assertEqual(arr, [2, 2, 2, 2, 2])

    def test_mixed_positive_negative(self):
        arr = [3, -1, 4, -1, 5, -9, 2, 6, 5, 3, 5]
        quickSort(arr)
        self.assertEqual(arr, sorted(arr))

    def test_large_numbers(self):
        arr = [1_000_000, 5, 2_000_000, 1, -1_000_000]
        quickSort(arr)
        self.assertEqual(arr, sorted(arr))


if __name__ == "__main__":
    unittest.main()
