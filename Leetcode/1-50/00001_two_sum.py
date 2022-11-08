"""
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List


def two_sum3(nums, target):
    """
    key problem: must one in previous and another one is behind
    use a temporary dict save left value and its index
    """
    temp_dict = {}
    for i, v in enumerate(nums):
        left = target - v
        if v in temp_dict:
            return [temp_dict[v], i]
        temp_dict[left] = i
    return []


def two_sum(nums: List[int], target: int) -> List[int]:
    for index, value in enumerate(nums):
        left = target - value
        for sub_index, sub_value in enumerate(nums[index+1:]):
            if left == sub_value:
                return [index, index+sub_index+1]
    return []


def two_sum2(nums: List[int], target: int) -> List[int]:
    nums_nums = len(nums)
    for index, value in enumerate(nums):
        for i in range(index+1, nums_nums):
            if target - nums[index] - nums[i] == 0:
                return [index, i]
    return []


if __name__ == '__main__':
    Nums1 = [2, 7, 11, 15]
    Target1 = 9

    Nums2 = [3, 2, 4]
    Target2 = 6

    # data = two_sum2(Nums2, Target2)
    data = two_sum3(Nums1, Target1)
    print(data)
