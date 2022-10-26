"""
Description:
Author:qxy
Date: 2019-07-04 18:59
File: radix_sort 
"""


def radix_sort(mylist):
    base = 10
    n = 0
    max_digit = len(str(max(mylist)))

    while max_digit > n:
        bucket = [[] for _ in range(10)]
        for i in mylist:
            # print(i)
            # print(i // (base ** n))
            # print(i // (base ** n) % 10)
            bucket[i // (base ** n) % 10].append(i)
        # print(bucket)
        index = 0
        for i in range(len(bucket)):
            stage_two = bucket[i]
            print(stage_two)
            for nums in stage_two:
                # print(nums)
                mylist[index] = nums
                index += 1
            print('-----')
        n += 1
    # print(mylist)


radix_sort([1001, 800, 404, 55, 666])