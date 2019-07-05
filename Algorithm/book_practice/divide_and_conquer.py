"""
Description:
Author:qxy
Date: 2019-06-05 19:06
File: divide_and_conquer 
"""


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        base = array[0]
        less = [x for x in array[1:] if x <= base]
        greater = [x for x in array[1:] if x > base]
        print(less, base, greater)
        return quicksort(less) + [base] + quicksort(greater)


quicksort([1, 6, 7, 3, 2])