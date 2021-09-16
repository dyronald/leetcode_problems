from typing import List
from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = set()
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1

        keys = sorted(map.keys())
        
        if map.get(0, 0) >= 3:
            result.add((0, 0, 0))

        for i in range(len(keys)-1):
            if keys[i] >= 0:
                break

            for j in range(i+1, len(keys)):
                diff = 0 - (keys[i]+keys[j])
                if diff < keys[j]:
                    break
                if diff in map and (diff != keys[j] or map[diff]>1):
                    result.add((keys[i], keys[j], diff))
            
            if map[keys[i]] >= 2:
               diff = 0 - (keys[i]*2)
               if diff > keys[i] and diff in map:
                   result.add((keys[i], keys[i], diff))

        return list(result)
    
    def threeSum_old(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = set()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            elif nums[i] == 0 and (0, 0, 0) in result:
                break
            for j in range(i+1, len(nums)-1):
                diff = 0 - (nums[i] + nums[j])
                if self._is_in_list(diff, j+1, nums):
                    result.add((nums[i], nums[j], diff))

        return list(result)
    
    def _is_in_list(self, val, lo, nums):
        idx = bisect_left(nums, val, lo=lo)
        return idx < len(nums) and nums[idx] == val
