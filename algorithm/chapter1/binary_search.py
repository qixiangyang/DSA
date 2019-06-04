"""
Description:
Author:qxy
Date: 2019-06-04 23:01
File: binary_search 
"""

"""
二分法查找数据
"""


def binary_search(list_data, num):
    low = 0
    high = len(list_data) -1

    while low <= high:
        mid = int((low + high) / 2) - 1

        if num == list_data[mid]:
            return mid

        elif num < list_data[mid]:
            high = mid

        elif num > list_data[mid]:
            low = mid

    return None


data = binary_search([1, 3, 5, 7, 9], -1)


