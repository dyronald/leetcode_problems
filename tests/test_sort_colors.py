import unittest
from sort_colors import Solution

class Test(unittest.TestCase):
    def test_public_method_exists(self):
        s = Solution()
        result = s.sortColors([0])
        self.assertIsNone(result)

    def test_sorted_input(self):
        s = Solution()
        input = [0, 0, 1, 1, 2, 2]
        expected = input.copy()

        s.sortColors(input)
        self.assertEqual(expected, input)

    def test_single_value(self):
        s = Solution()
        input = [2]
        expected = input.copy()

        s.sortColors(input)
        self.assertEqual(expected, input)

    def test_sorting(self):
        s = Solution()
        input = [2, 1, 1, 0, 2, 0, 0]
        expected = [0, 0, 0, 1, 1, 2, 2]

        s.sortColors(input)
        self.assertEqual(expected, input)

    def test_sorting_2_values(self):
        s = Solution()
        input = [2, 0, 2, 0, 0]
        expected = [0, 0, 0, 2, 2]

        s.sortColors(input)
        self.assertEqual(expected, input)

    def test_empty(self):
        s = Solution()
        input = []
        s.sortColors(input)
        self.assertEqual([], input)
