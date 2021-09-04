import unittest
from subsets import Solution


class Test(unittest.TestCase):
    def test_list_size_3(self):
        s = Solution()
        result = s.subsets([1, 2, 3])
        self.compare_unordered(
            result, [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        )

    def test_single_element(self):
        s = Solution()
        result = s.subsets([1])
        self.compare_unordered(result, [[], [1]])

    def test_10_elements_does_not_freeze(self):
        s = Solution()
        s.subsets([1,2,3,4,5,6,7,8,9,0])

    def compare_unordered(self, result, expected):
        result_uo = [set(r) for r in result]
        expected_uo = [set(e) for e in expected]

        self.assertEqual(len(result), len(expected))

        for r in result_uo:
            self.assertIn(r, expected_uo)
