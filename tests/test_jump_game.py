import unittest
from jump_game import Solution


class TestJumpGame(unittest.TestCase):
    def test_can_jump_in_single_step(self):
        s = Solution()
        result = s.canJump([1, 1])
        self.assertTrue(result)

    def test_cant_jump_from_start(self):
        s = Solution()
        result = s.canJump([0, 1])
        self.assertFalse(result)

    def test_can_jump_multi_step(self):
        s = Solution()
        result = s.canJump([1, 1, 0])
        self.assertTrue(result)

    def test_cant_jump_multi_step(self):
        s = Solution()
        result = s.canJump([2, 1, 0, 3, 4, 5])
        self.assertFalse(result)

    def test_nums_size_1(self):
        s = Solution()
        result = s.canJump([0])
        self.assertTrue(result)
