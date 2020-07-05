"""

"""
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    if not nums: return 0
    start = 0
    end = len(nums) - 1

    while start < end:
        if nums[start] != val:
            start += 1
        elif nums[start] == val and nums[end] == val:
            end -= 1
        else:
            nums[start], nums[end] = nums[end], nums[start]

    if nums[start] == val:
        return start
    else:
        return start + 1

print(removeElement([0,1,2,2,3,0,4,2], 2))


