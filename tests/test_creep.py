import unittest
import creep
from typing import List
from dataclasses import dataclass

class Test(unittest.TestCase):
    @dataclass
    class Input:
        input: List[int]
        target: int
        start: int
        end: int

    inputs = [
        Input([1, 2, 3, 4, 4, 4, 4, 5], 4, 3, 6),
        Input([1, 1, 1, 4, 4, 4, 4, 5], 1, 0, 2),
        Input([1, 2, 3, 4, 4, 4, 4, 5], 1, 0, 0),
        Input([1, 2, 3, 4, 4, 4, 4, 5, 6], 4, 3, 6),
        Input([1, 1, 1, 4, 4, 4, 4, 5, 6], 1, 0, 2),
        Input([1, 2, 3, 4, 4, 4, 4, 5, 6], 1, 0, 0),
        Input([1, 2, 3, 4, 4, 4, 5, 6], 4, 3, 5),
        Input([1, 2, 3, 4, 5], 5, 4, 4),
        Input([1, 2, 3, 4, 5, 5, 5], 5, 4, 6),
        Input([1, 2, 3, 4, 5], 6, -1, -1),
        Input([1], 1, 0, 0),
        Input([1], 2, -1, -1),
    ]

    def test_find_start(self):
        for i in self.inputs:
            self.assertEqual(i.start, creep.find_start(i.input, i.target))

    def test_find_end(self):
        for i in self.inputs:
            self.assertEqual(i.end, creep.find_end(i.input, i.target))

