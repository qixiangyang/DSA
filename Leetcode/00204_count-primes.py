"""
Description:
Author:qxy
Date: 2019/11/18 11:29 下午
File: 00204 
"""

"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

"""
埃氏筛
"""

import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        label_list = [1] * n
        label_list[0] = label_list[1] = 0

        for i in range(2, int(n**0.5) + 1):
            if label_list[i] == 1:
                label_list[i*i:n:i] = [0] * len(label_list[i*i:n:i])
        return sum(label_list)


a = Solution()
res = a.countPrimes(0)
print(res)


