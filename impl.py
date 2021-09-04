def find_start(nums):
    first = nums[0]

    if first <= nums[-1]:
        return 0

    window_start = 1
    window_end = len(nums) - 1

    # index points to target on exit or -1
    while window_start != window_end:
        index = window_start + (window_end - window_start) // 2
        val = nums[index]

        if val > first:
            window_start = index + 1
        elif val < first:
            window_end = index
    
    return window_start

def find_num(nums, target):
    window_start = 0
    window_end = len(nums) - 1

    # index points to target on exit or -1
    while True:
        index = window_start + ((window_end - window_start) // 2)
        val = nums[index]

        if window_start == window_end and val != target:
            index = -1
            break

        if val > target:
            window_end = index
        elif val < target:
            window_start = index + 1
        else:
            # target found
            break

    return index


def search(nums, target):
    start = find_start(nums)

    if start == 0:
        return find_num(nums, target)
    elif target < nums[0]:
        found = find_num(nums[start:], target)
        if found >= 0:
            return found + start
        return found
    else:
        return find_num(nums[:start], target)
