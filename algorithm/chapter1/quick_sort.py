"""
Description:
Author:qxy
Date: 2019-06-05 16:30
File: quick_sort 
"""


def sort_list(arr):
    smallest_value = arr[0]
    smallest_index = 0

    for index, value in enumerate(arr):
        if smallest_value > value:
            smallest_value = arr[index]
            smallest_index = index

    return smallest_index


def selectionSort(arr):

    result_list = []

    for i in range(len(arr)):
        smallest_index = sort_list(arr)
        result_list.append(arr[smallest_index])
        arr.pop(smallest_index)
    return result_list


print(selectionSort([5, 3, 6, 2, 10]))










