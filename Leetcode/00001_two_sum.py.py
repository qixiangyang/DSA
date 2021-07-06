"""
题目：
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 暴力计算
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    data_len = len(nums)

    for i, num in enumerate(nums):
        for m in range(i+1, data_len):
            temp = nums[i] + nums[m]
            if temp == target:
                return [i+1, m+1]


nums = [2, 7, 11, 15]
target = 9

data = twoSum(nums, target)
print(data)


# hash
def twoSum2(nums, target):

    temp_dict = {}

    for i, v in enumerate(nums):
        left = target - v
        if v in temp_dict.keys():
            return [temp_dict[v], i]
        temp_dict[left] = i
        print(temp_dict)
    return []


nums = [1, 2, 3, 5]
data = twoSum2(nums, 6)
print(data)