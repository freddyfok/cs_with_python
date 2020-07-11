"""
Given a list of int, find the max sum of a subarray
[-2,1,-3,4,-1,2,1,-5,4]

sum the previous sums (0 if it was -ve) and current value
pick the max between that sum and current value
reset the sum by max between sum and 0
"""
import math
from typing import List


def max_subarray(n: List):
    ans = -math.inf
    sum_ = 0
    for i in n:
        sum_ += i
        ans = max(ans, sum_)
        sum_ = max(sum_, 0)
    return ans

