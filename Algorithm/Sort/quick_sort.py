"""
Description:
Author:qxy
Date: 2019-07-03 16:08
File: quick_sort 
"""


def q_sort1(list_data):
    if not list_data:
        return []
    else:
        pivot = list_data[0]
        l = [x for x in list_data if x < pivot]
        r = [x for x in list_data[1:] if x >= pivot]
        print(pivot)
        print(l)
        print(r)
    return q_sort1(l) + [pivot] + q_sort1(r)


list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
data = q_sort1(list_data)

print(data)