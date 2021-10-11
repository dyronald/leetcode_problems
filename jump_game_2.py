from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        jumps = 1
        cursor = 1
        end_index = len(nums) - 1
        max_pos = nums[0]

        while max_pos < end_index:
            tmp_max_pos = max_pos
            while cursor <= max_pos:
                tmp_max_pos = max(tmp_max_pos, nums[cursor]+cursor)
                cursor += 1
            max_pos = tmp_max_pos
            jumps += 1

        return jumps
