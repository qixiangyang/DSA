"""
Description:
Author:qxy
Date: 2019-08-13 16:23
File: fib_dp 
"""
import time
from functools import wraps


def memo(func):
    cache = dict()

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fib(n):

    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


# dp fib
def fib_db(n):

    if n < 2:
        return n

    res = 0
    prev, p_prev = 1, 0
    i = 2
    while i <= n:
        res = prev + p_prev
        prev, p_prev = res, prev
        i += 1
    return res


def new_fib(n):
    if n < 2:
        return n

    i_now = 1
    i_pre = 0
    i = 2
    while i <= n:
        i_now, i_pre = i_now + i_pre, i_now
        i += 1
    return i_now


n = 11

t1 = time.time()
print(fib(n))
t2 = time.time()
print(f"fib(100) cost {str(t2-t1)}")
print(fib_db(n))
t3 = time.time()
print(f"fib(100) cost {str(t3-t2)}")


print(new_fib(n))