"""
给定不同面额的硬币 coins 和一个总金额 amount。
编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

 
示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 

说明:
你可以认为每种硬币的数量是无限的。
"""
from functools import lru_cache


def change_coin(coins: list, amount: int):

    # @lru_cache()
    def dp(n):
        memo = dict()
        if n == 0:
            return 0
        if n < 0:
            return -1

        res = float('INF')
        for coin in coins:
            sub = dp(n-coin)
            if sub < 0:
                continue
            res = min(res, sub + 1)

        memo[n] = res if res != float('INF') else - 1
        return memo[n]

    return dp(amount)


if __name__ == '__main__':
    print(change_coin(coins=[1,3,5], amount=11))