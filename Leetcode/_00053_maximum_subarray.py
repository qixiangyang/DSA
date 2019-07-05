"""
Description:
Author:qxy
Date: 2019-06-09 14:21
File: 00053_maximum_subarray 
"""

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

"""


def maxSubArray(nums) -> int:

    index_list = []
    for index, value in enumerate(nums):
        if value > 0:
            index_list.append(index)


    for i in range(len(index_list)-1):
        if index_list[i+1] - index_list[i] == 1:
            pass


