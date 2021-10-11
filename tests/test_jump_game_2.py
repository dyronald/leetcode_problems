import unittest
from jump_game_2 import Solution

class Test(unittest.TestCase):
    def test_basic_happy(self):
        s = Solution()
        output = s.jump([2,3,1,1,4])
        self.assertEqual(output, 2)

    def test_length_1(self):
        s = Solution()
        output = s.jump([0])
        self.assertEqual(output, 0)

    def test_pick_big_jump(self):
        s = Solution()
        output = s.jump([3,1,3,1,5,1,1,1,1,20,1,1,1,1,1])
        self.assertEqual(output, 4)

    def test_zeros(self):
        s = Solution()
        output = s.jump([3,0,0,1,5,0,1,0,1,1,1,1,1,1,1])
        self.assertEqual(output, 8)

    def test_pick_furthest(self):
        s = Solution()
        output = s.jump([3,2,2,2,1,3,1,1])
        self.assertEqual(output, 3)