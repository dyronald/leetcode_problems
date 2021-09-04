import unittest
from reverse_words import Solution


class Test(unittest.TestCase):
    def test_method_callable(self):
        s = Solution()
        s.reverse_words('hello world')

    def test_returns_str(self):
        s = Solution()
        result = s.reverse_words('hello world')
        self.assertTrue(isinstance(result, str))

    def test_reverse_2_words(self):
        s = Solution()
        result = s.reverse_words('hello world')
        self.assertEqual('world hello', result)

    def test_reverse_5_words(self):
        s = Solution()
        result = s.reverse_words('hello a b c world')
        self.assertEqual('world c b a hello', result)

    def test_multiple_spaces_between_words(self):
        s = Solution()
        result = s.reverse_words('hello    a   b c world')
        self.assertEqual('world c b a hello', result)

    def test_leading_trailing_spaces_in_input(self):
        s = Solution()
        result = s.reverse_words('     hello a b c world     ')
        self.assertEqual('world c b a hello', result)
