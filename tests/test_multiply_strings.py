import unittest
from multiply_strings import Solution

class Tests(unittest.TestCase):
    def test_1_digit(self):
        s = Solution()
        ans = s.multiply('9', '9')
        self.assertEqual(ans, '81')

    def test_3_digits(self):
        s = Solution()
        ans = s.multiply('999', '999')
        self.assertEqual(ans, '998001')

    def test_3_different_digits(self):
        s = Solution()
        ans = s.multiply('123', '456')
        self.assertEqual(ans, '56088')

    def test_both_zero(self):
        s = Solution()
        ans = s.multiply('0', '0')
        self.assertEqual(ans, '0')

    def test_zero(self):
        s = Solution()
        ans = s.multiply('123456789', '0')
        self.assertEqual(ans, '0')

    def test_zero_mid_digits(self):
        s = Solution()
        ans = s.multiply('1000', '100')
        self.assertEqual(ans, '100000')
