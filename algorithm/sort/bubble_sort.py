"""
Description:
Author:qxy
Date: 2019-06-29 14:50
File: bubble_sort 
"""

from timeit import Timer


def bubble_sort():
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    for i in range(len(list_data)-1, 0, -1):
        for j in range(i):
            if list_data[j] > list_data[j+1]:
                list_data[j], list_data[j+1] = list_data[j+1], list_data[j]


# bubble_sort(li)
# print(li)

t1 = Timer("bubble_sort()", "from __main__ import bubble_sort")
print("concat ", t1.timeit(number=1000), "seconds")


