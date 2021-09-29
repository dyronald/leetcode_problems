from typing import List
from bisect import bisect


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i >= 0:
            i -= 1
            if nums[i] < nums[i+1]:
                break
        
        if i < 0:
            nums.reverse()
        else:
            start = i + 1
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

            j = bisect(nums, nums[i], i+1)
            nums[i], nums[j] = nums[j], nums[i]
