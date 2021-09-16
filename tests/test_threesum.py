import unittest
from threesum import Solution


class Test(unittest.TestCase):
    def test_example(self):
        s = Solution()
        result = s.threeSum(nums=[-1,0,1,2,-1,-4])
        self.compare_unordered(
            result, [[-1,-1,2],[-1,0,1]]
        )

    def test_repeated_positive(self):
        s = Solution()
        result = s.threeSum(nums=[1,1,-2])
        self.compare_unordered(
            result, [[-2,1,1]]
        )

    def test_nums_len_2(self):
        s = Solution()
        result = s.threeSum(nums=[-1,0])
        self.assertEqual(0, len(result))

    def test_no_hits(self):
        s = Solution()
        result = s.threeSum(nums=[0,1,0,1,2,3,4,5,6,7,8])
        self.assertEqual(0, len(result))

    def test_no_identical_triples(self):
        s = Solution()
        result = s.threeSum(nums=[-3,-3,-3,1,4,4,4,4,4,4,4])
        self.compare_unordered(
            result, [[-3,1,4]]
        )

    def compare_unordered(self, result, expected):
        result_uo = [set(r) for r in result]
        expected_uo = [set(e) for e in expected]

        self.assertEqual(len(result), len(expected))

        for r in result_uo:
            self.assertIn(r, expected_uo)
