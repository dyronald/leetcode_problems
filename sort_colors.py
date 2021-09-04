from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = {
            0: 0,
            1: 0,
            2: 0
        }
        for n in nums:
            counts[n] += 1

        for i in range(counts[0]):
            nums[i] = 0
        for i in range(counts[0], counts[0]+counts[1]):
            nums[i] = 1
        for i in range(counts[0]+counts[1], counts[0]+counts[1]+counts[2]):
            nums[i] = 2
