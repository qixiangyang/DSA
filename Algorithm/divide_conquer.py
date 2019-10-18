"""
Description:
Author:qxy
Date: 2019/10/18 3:59 下午
File: divide_conquer 
"""

from typing import List

"""
快排
时间复杂度nlog(n)
"""


def part(nums: List):
    pivot = nums[0]
    left = [x for x in nums if x < pivot]
    right = [x for x in nums if x > pivot]

    return left, pivot, right


def fast_sort(nums: List) -> List:
    if len(nums) <= 1:
        return nums
    left, pivot, right = part(nums)

    return fast_sort(left) + [pivot] + fast_sort(right)


ls = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
res = fast_sort(ls)
print(res)


