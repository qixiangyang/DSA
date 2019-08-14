"""
Description:
Author:qxy
Date: 2019-08-13 16:23
File: fib_dp 
"""


def fib(n):

    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)


print(fib(100))


from functools import wraps


def memo(func):
    cache = dict()

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)

        return cache[args]
    return wrap


fib = memo(fib)
print(fib(100))