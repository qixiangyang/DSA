"""
Description:
Author:qxy
Date: 2019/10/18 3:59 下午
File: divide_conquer 
"""

from typing import List
"""
https://zhuanlan.zhihu.com/p/44213575
"""


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


# ls = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
# res = fast_sort(ls)
# print(res)


"""
并归排序
时间复杂度log(n)
具体过程可以通过逐步执行来学习，参见以下网址
http://pythontutor.com/visualize.html#mode=display
"""


def merge_sort(nums: List) -> List:

    mid = len(nums) // 2

    left = nums[:mid]
    right = nums[mid:]

    if len(left) > 1:
        left = merge_sort(left)

    if len(right) > 1:
        right = merge_sort(right)

    res = []
    while left and right:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    return res + (left or right)


lis = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
data = merge_sort(lis)
print(data)


