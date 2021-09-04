import unittest
from rotate import Coord, Solution

class TestRotate(unittest.TestCase):
    def test_top(self):
        s = Solution()
        self.assertEqual(
            Coord(0, 0),
            s.top(4, 0, 0))
        self.assertEqual(
            Coord(1, 0),
            s.top(4, 0, 1))
        self.assertEqual(
            Coord(1, 1),
            s.top(4, 1, 0))
        self.assertEqual(
            Coord(2, 1),
            s.top(4, 1, 1))

    def test_right(self):
        s = Solution()
        self.assertEqual(
            Coord(3, 0),
            s.right(4, 0, 0))
        self.assertEqual(
            Coord(3, 1),
            s.right(4, 0, 1))
        self.assertEqual(
            Coord(2, 1),
            s.right(4, 1, 0))
        self.assertEqual(
            Coord(2, 2),
            s.right(4, 1, 1))

    def test_bottom(self):
        s = Solution()
        self.assertEqual(
            Coord(3, 3),
            s.bottom(4, 0, 0))
        self.assertEqual(
            Coord(2, 3),
            s.bottom(4, 0, 1))
        self.assertEqual(
            Coord(2, 2),
            s.bottom(4, 1, 0))
        self.assertEqual(
            Coord(1, 2),
            s.bottom(4, 1, 1))

    def test_left(self):
        s = Solution()
        self.assertEqual(
            Coord(0, 3),
            s.left(4, 0, 0))
        self.assertEqual(
            Coord(0, 2),
            s.left(4, 0, 1))
        self.assertEqual(
            Coord(1, 2),
            s.left(4, 1, 0))
        self.assertEqual(
            Coord(1, 1),
            s.left(4, 1, 1))

    def test_rotate(self):
        s = Solution()
        self.assertEqual(
            [[7,4,1],[8,5,2],[9,6,3]],
            s.rotate([[1,2,3],[4,5,6],[7,8,9]]))
        self.assertEqual(
            [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]],
            s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
        self.assertEqual(
            [
                [21,16,11, 6, 1],
                [22,17,12, 7, 2],
                [23,18,13, 8, 3],
                [24,19,14, 9, 4],
                [25,20,15,10, 5]
            ],
            s.rotate(
                [
                    [ 1, 2, 3, 4, 5],
                    [ 6, 7, 8, 9,10],
                    [11,12,13,14,15],
                    [16,17,18,19,20],
                    [21,22,23,24,25]
                ]
            ))

