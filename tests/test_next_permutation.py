import unittest
from next_permutation import Solution


class Test(unittest.TestCase):
    def test_basic(self):
        s = Solution()
        nums = [1,2,3]
        expected = [
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1],
            [1,2,3],
        ]

        for e in expected:
            s.nextPermutation(nums)
            self.assertEqual(e, nums)

    def test_basic_with_duplicate_elem(self):
        s = Solution()
        nums = [1,1,5]
        expected = [
            [1,5,1],
            [5,1,1],
            [1,1,5],
        ]

        for e in expected:
            s.nextPermutation(nums)
            self.assertEqual(e, nums)

    def test_middle_swap(self):
        s = Solution()
        nums = [1,1,2,2,5,5,4,4,3,3]
        s.nextPermutation(nums)
        self.assertEqual([1,1,2,3,2,3,4,4,5,5], nums)

    def test_sorted(self):
        s = Solution()
        nums = [3,2,1]
        s.nextPermutation(nums)
        self.assertEqual([1,2,3], nums)

    def test_size_1(self):
        s = Solution()
        nums = [1]
        s.nextPermutation(nums)
        self.assertEqual([1], nums)
