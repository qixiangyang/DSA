"""
Description:
Author:qxy
Date: 2019-06-29 16:12
File: insert_sort 
"""

"""
之后再解决
"""


def insert_sort(arr):
    length = len(arr)
    for i in range(1, length):
        x = arr[i]
        for j in range(i, -1, -1):
            # j为当前位置，试探j-1位置
            if x < arr[j]:
                arr[j] = arr[j]
            else:
                # 位置确定为j
                arr[j] = x
                break


list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
"""
[26, 54, 93, 17, 77, 31, 44, 55, 20]
"""
insert_sort(list_data)

print(list_data)
