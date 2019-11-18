"""
Description:
Author:qxy
Date: 2019/10/18 3:59 下午
File: divide_conquer 
"""

from typing import (List)
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


# lis = [7, 5, 0, 6, 3, 4, 1, 9, 8, 2]
# data = merge_sort(lis)
# print(data)

"""
#O(nlogn)
#基本子算法（内置算法）
#虽然也可以处理大数组，这里用于解决分治问题规模小于2时候
"""


def get_max(nums: List) -> int:
    return max(nums)


def solve(nums: List):
    if len(nums) <= 2:
        return get_max(nums)

    left, right = nums[:len(nums) // 2], nums[len(nums) // 2:]
    max_left, max_right = solve(left), solve(right)

    return get_max([max_left, max_right])


"""
判断元素是否存在
"""


def is_in_it(nums: List, num: int)-> True or False:
    if len(nums) <= 2:
        if num in nums:
            return True
    else:
        return False

    left, right = nums[:len(nums) // 2], nums[len(nums) // 2:]
    max_left, max_right = is_in_it(left, num), is_in_it(right, num)

    if max_left or max_right:
        pass


lis = [12,2,23,45,67,3,2,4,45,63,24,23]
#查找
print(is_in_it(lis, 45)) #YES~
print(is_in_it(lis, 5))  #NOT~
