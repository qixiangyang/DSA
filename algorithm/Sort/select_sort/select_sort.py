"""
Description:
Author:qxy
Date: 2019-06-29 15:18
File: select_sort 
"""


def select_sort(data_list):

    for i in range(len(data_list)-1, -1, -1):
        max_index = 0
        for m in range(i+1):
            if data_list[m] >= data_list[max_index]:
                max_index = m
        data_list[i], data_list[max_index] = data_list[max_index], data_list[i]


list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
select_sort(list_data)
print(list_data)