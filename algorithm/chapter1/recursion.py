"""
Description:
Author:qxy
Date: 2019-06-05 17:48
File: recursion 
"""

"""
递归学习整理，
递归本质上是一个调用栈，递归需要占据栈空间，因此，递归次数多时，需要使用循环，或者尾递归
递归需要一个基线条件，保证递归能够现在约束的情况下下返回想要的数据

"""

def countdown(i):
    print(i)
    if i <= 0:
        return False
    else:
        return countdown(i-1)


countdown(10)


def fact(x):

    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

print(fact(5))

