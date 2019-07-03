"""
Description:
Author:qxy
Date: 2019-06-29 16:12
File: insert_sort 
"""


def insert_sort(list_data):

    for i in range(len(list_data)-1, -1, -1):
        for m in range(1, i):
            if list_data[m-1] <= list_data[i] <= list_data[m+1]:
                value = list_data[i]
                list_data.pop(i)
                list_data.insert(m, value)
        print(list_data)


list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(list_data)

print(list_data)
