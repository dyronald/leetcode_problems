from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subsets_recurse(nums, [])

    def subsets_recurse(self, nums, accumulated):
        subsets = [accumulated]

        while len(nums) > 0:
            popped = nums.pop()
            rec = self.subsets_recurse(nums[:], [*accumulated, popped])
            subsets.extend(rec)

        return subsets
