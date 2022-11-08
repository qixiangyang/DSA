"""
Description:
Author:qxy
Date: 2019-06-11 19:39
File: 00202_happy_number 
"""

"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

"""
考虑数字个数
"""

def isHappy(n):

    # if n == 1:
    #     return True
    #
    # else:
    #     result = 0
    #     for i in list(str(n)):
    #         result += int(i) ** 2
    #     return isHappy(result)

    count = 0

    while n != 1:
        x = 0
        for i in list(str(n)):
            x += int(i) ** 2
        n = x
        count += 1
        if count > 10:
            return False
    return True


print(isHappy(2))