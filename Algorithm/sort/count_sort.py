"""
Description:
Author:qxy
Date: 2019-07-04 17:58
File: count_sort 
"""


def count_sort(list_data):

    tmp_list = []

    for i in list_data:
        count = 0
        for m in list_data:
            if i > m:
                count += 1

        tmp_list.append([count, i])

    # print(tmp_list)
    res = []

    for i in range(len(list_data)):
        for m in tmp_list:
            if i == m[0]:
                res.append(m[0])
    return res


list_data = [5, 6, 3, 2, 1, 65, 2, 0, 8, 0]
res = count_sort(list_data)
print(res)