"""
Description:
Author:qxy
Date: 2019-06-10 13:56
File: 00088_merge_sorted_array 
"""

"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]


"""


def merge(nums1, m: int, nums2, n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    num1 = nums1[:m] + nums2
    num1 = sorted(num1)

    print(num1)


merge([1,2,3,0,0,0], 3, [2,5,6], 3)