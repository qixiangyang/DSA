"""
Description:
Author:qxy
Date: 2019-06-04 15:53
File: digui 
"""
from typing import List

# # 阶乘
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# # 吃桃子
# def peach(n):
#     if n == 1:
#         return 1
#     return (peach(n-1)+1) * 2
#
#
# # 逆序放数
# s = '1234'
# lengh = len(s)
#
#
# def reverse_list(lengh, res=[]):
#     if lengh == 0:
#         return res
#     res.append(s[lengh-1])
#     return reverse_list(lengh-1, res)
#
#
# data = reverse_list(lengh)


# 斐波拉契数列

def fib_list(n):
    if n == 0:
        return 0
    if n < 3:
        return 1
    return fib_list(n-1) + fib_list(n-2)


print(fib_list(10))
