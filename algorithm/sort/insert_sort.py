"""
Description:
Author:qxy
Date: 2019-06-29 16:12
File: insert_sort 
"""

"""
之后再解决
"""


def insert_sort(list_data):

    for i in range(len(list_data)):
        for m in range(i, 0, -1):
            if list_data[m] < list_data[m-1]:
                list_data[m], list_data[m-1] = list_data[m-1], list_data[m]

list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(list_data)

print(list_data)
