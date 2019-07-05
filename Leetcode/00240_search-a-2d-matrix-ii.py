"""
Description:
Author:qxy
Date: 2019-06-24 19:18
File: 00240_search-a-2d-matrix-ii 
"""

"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。
"""


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    def binary_search(lis, num):
        left = 0
        right = len(lis)-1
        while left <= right:  # 循环条件
            mid = (left + right) // 2  # 获取中间位置，数字的索引（序列前提是有序的）
            if num < lis[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找，
                right = mid - 1  # 来到左边后，需要将右变的边界换为mid-1
            elif num > lis[mid]:  # 如果查询数字比中间数字大，那么去二分后的右边找
                left = mid + 1  # 来到右边后，需要将左边的边界换为mid+1
            else:
                return True  # 如果查询数字刚好为中间值，返回该值得索引
        return False  # 如果循环结束，左边大于了右边，代表没有找到

    for i in matrix:
        status = binary_search(i, target)
        if status is not False:
            return True
    return False

# print(int(1.5))

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

# matrix = [[1,1]]

print(searchMatrix(matrix, 5))


# def binary_search(list_data, num):
#     low = 0
#     high = len(list_data) - 1
#     count = 1
#
#     while low <= high:
#         mid = int((low + high) / 2) - 1
#
#         if num == list_data[mid]:
#             return True
#
#         elif num < list_data[mid]:
#             high = mid
#
#         elif num > list_data[mid]:
#             low = mid
#
#
# data = binary_search([2,   5,  8, 12, 19], 5)
# print(data)