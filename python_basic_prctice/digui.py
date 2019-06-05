"""
Description:
Author:qxy
Date: 2019-06-04 15:53
File: digui 
"""


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(120))