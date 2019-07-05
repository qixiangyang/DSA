"""
Description:
Author:qxy
Date: 2019-07-03 17:29
File: merge_sort 
"""


def merge_sort(list_data):

    data_len = len(list_data)

    if data_len < 2:
        return list_data
    mid = int(data_len/2)

    left = merge_sort(list_data[:mid])
    right = merge_sort(list_data[mid:])

    print(left, right)

    return merge(left, right)


def merge(left, right):
    l = 0
    r = 0
    result = []

    while l < len(left) and r < len(right):

        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]

    return result


list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]

data = merge_sort(list_data)
print(data)

