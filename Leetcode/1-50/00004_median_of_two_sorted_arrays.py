"""
Description:
Author:qxy
Date: 2019-06-23 16:41
File: 00004_median_of_two_sorted_arrays 
"""

"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
"""
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    if len(nums1) > len(nums2):
        temp = nums2
        temp_o = nums1
    else:
        temp = nums1
        temp_o = nums2

    def inser_data(temp):



    lenth = len(temp_o)

    if len(temp_o) % 2 == 0:
        return (temp_o[(int(lenth/2)-0.5)] + temp_o[(int(lenth/2)+0.5)])/2
    else:
        return temp_o[int(lenth/2)]


print(findMedianSortedArrays([1, 2], [3, 4]))



