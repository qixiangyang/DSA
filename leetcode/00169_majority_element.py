"""
Description:
Author:qxy
Date: 2019-06-24 17:12
File: 00_169_majority_element 
"""

"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""

from typing import List
from collections import defaultdict


def majorityElement(nums: List[int]) -> int:

    data = defaultdict(int)
    for i in nums:
        data[i] += 1
    # print(dir(data))
    data_list = sorted(data.items(), key=lambda x: x[1] ,reverse=True)
    return data_list[0][0]

print(majorityElement([2, 2, 1, 1, 1, 2, 2]))

