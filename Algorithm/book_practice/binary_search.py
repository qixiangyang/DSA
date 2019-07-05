"""
Description:
Author:qxy
Date: 2019-06-04 23:01
File: binary_search 
"""

"""
二分法查找数据
"""


# def binary_search(list_data, num):
#     low = 0
#     high = len(list_data) - 1
#
#     while low <= high:
#         mid = int((low + high) / 2) - 1
#
#         if num == list_data[mid]:
#             return mid
#
#         elif num < list_data[mid]:
#             high = mid
#
#         elif num > list_data[mid]:
#             low = mid
#
#     return None

def binary_search(lis, num):
    left = 0
    right = len(lis) - 1
    while left <= right:  # 循环条件
        mid = (left + right) // 2  # 获取中间位置，数字的索引（序列前提是有序的）
        if num < lis[mid]:  # 如果查询数字比中间数字小，那就去二分后的左边找，
            right = mid - 1  # 来到左边后，需要将右变的边界换为mid-1
        elif num > lis[mid]:  # 如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1  # 来到右边后，需要将左边的边界换为mid+1
        else:
            return True  # 如果查询数字刚好为中间值，返回该值得索引
    return False  # 如果循环结束，左边大于了右边，代表没有找到


data = binary_search([1, 4, 7, 11, 15], 5)
print(data)

