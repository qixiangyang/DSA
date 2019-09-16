"""
Description:
Author:qxy
Date: 2019/9/16 7:39 下午
File: 00034 
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        data_len = len(nums)
        mid = data_len // 2
        r_index = -1
        r_mid = (mid + data_len-1) // 2
        while mid < r_mid < data_len-1:
            if nums[r_mid] == target:
                r_index = mid
                mid = (mid + data_len) // 2
            elif nums[r_mid] > target:
                data_len = r_mid
            elif nums[r_mid] < target:
                mid = (r_mid + data_len) // 2

        l_index = -1
        l_mid = mid // 2
        while 0 < l_mid <= mid:
            if nums[l_mid] == target:
                l_index = mid
                mid = mid // 2
            elif nums[l_mid] > target:
                mid = l_mid
            elif nums[l_mid] < target:
                mid = l_mid // 2

        return [l_index, r_index]