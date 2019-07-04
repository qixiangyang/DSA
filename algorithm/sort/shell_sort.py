"""
Description:
Author:qxy
Date: 2019-07-04 17:08
File: shell_sort 
"""


def shell_sort(list_data):
    n = len(list_data)
    gap = n // 2
    while gap >= 1:
        print(gap)
        for i in range(gap, n):
            for m in range(i, 0, -gap):
                print(i, m)
                if list_data[m] < list_data[m-gap]:
                    list_data[m], list_data[m-gap] = list_data[m-gap], list_data[m]

        gap = gap // 2

    return list_data


numlist = [5,7,8,3,1,2,4,6,9]
print("排序前：%s"% numlist)
shell_sort(numlist)
print("排序后：%s"%numlist)

# for m in range(4, 0, -4):
#     print(m)