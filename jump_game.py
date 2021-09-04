class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True

        cur = len(nums) - 2
        min = 1

        while cur >= 0:
            if nums[cur] >= min:
                min = 1
            else:
                min += 1
            cur -= 1

        return nums[0] >= min
