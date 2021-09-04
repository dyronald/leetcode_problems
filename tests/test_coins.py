import unittest
from coins import Solution

class Tests(unittest.TestCase):
    def test_invoke_method(self):
        s = Solution()
        s.coinChange([1], 1)

    def test_combination_found(self):
        s = Solution()
        result = s.coinChange([1, 2, 5], 11)
        self.assertEqual(3, result)

    def test_combination_not_found(self):
        s = Solution()
        result = s.coinChange([5, 3, 10], 7)
        self.assertEqual(-1, result)

    def test_zero_sum(self):
        s = Solution()
        result = s.coinChange([1,2], 0)
        self.assertEqual(0, result)

    def test_100(self):
        s = Solution()
        result = s.coinChange([1,2, 5], 100)
        self.assertEqual(20, result)
