"""
Description:
Author:qxy
Date: 2019-07-04 17:29
File: bucket_sort 
"""


def bucket_sort(list_data):
    max_num = max(list_data)

    bucket = [0] * (max_num + 1)
    print(bucket)

    for i in list_data:
        bucket[i] += 1
    mm = []
    for index, value in enumerate(bucket):
        if value != 0:
            mm.extend([index] * value)

    return mm


list_data = [5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
mm = bucket_sort(list_data)
print(mm)
