"""
Description:
Author:qxy
Date: 2019-06-11 17:59
File: 00204_count_primes 
"""

"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""


def countPrimes(n: int) -> int:

    count = 0
    while n > 0:
        num = []
        for i in range(1, n):
            if n % i == 0:
                num.append(n)
        if len(num) == 2:
            count += 1
        print(num)

        n -= 1
    return count


print(countPrimes(4))