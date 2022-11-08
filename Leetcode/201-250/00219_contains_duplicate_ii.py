"""
Description:
Author:qxy
Date: 2019-06-10 14:22
File: 00219_contains_duplicate_ii 
"""

"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

"""


def containsNearbyDuplicate(nums, k: int) -> bool:

    data_dict = {}
    index = 0

    for value in nums:
        if data_dict.get(value) is not None:
            if index - data_dict[value] <= k:
                return True
        data_dict[value] = index
        index += 1

    return False


print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))