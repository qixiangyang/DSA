import functools


"""
Description:
Author:qxy
Date: 2019-06-09 16:30
File: 00070_climbing_stairs 
"""

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

"""
"""
仅仅考虑 n 前面 两个状态即可，仅需要计算 n-1 下及 n-2 下分别需要多少次，将这个问题转化为一个递归问题
"""

# def climb_stairs(stairs: int) -> int:
#
#     def dp(n):
#
#         sum_n = 0
#
#         if n < 0:
#             return -1
#         for s in [1, 2]:
#             sub = dp(n-s)
#             if sub == -1:
#                 continue
#             sum_n += 1
#         return sum_n
#
#     return dp(stairs)

@functools.lru_cache(100)
def climb_stairs(stairs: int) -> int:
    if stairs == 1:
        return 1
    if stairs == 2:
        return 2

    return climb_stairs(stairs-2) + climb_stairs(stairs - 1)


print(climb_stairs(100))


class Solution:
    @functools.lru_cache(100)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs(n - 1) + self.climbStairs(n - 2) if n > 2 else n

