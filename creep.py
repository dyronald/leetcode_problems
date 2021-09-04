import math


def find_start(nums, target):
    win_start = 0
    win_end = len(nums) - 1

    while win_start != win_end:
        index = win_start + ((win_end - win_start) // 2)
        val = nums[index]

        if val >= target:
            win_end = index
        else:
            win_start = index + 1

    if nums[win_start] != target:
        return -1
    return win_start


def find_end(nums, target):
    win_start = 0
    win_end = len(nums) - 1

    while win_start != win_end:
        index = win_start + (math.ceil((win_end - win_start) / 2))
        val = nums[index]

        if val <= target:
            win_start = index
        else:
            win_end = index - 1

    if nums[win_end] != target:
        return -1
    return win_end
