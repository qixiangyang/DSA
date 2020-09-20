from typing import List
from functools import lru_cache


"""
例子来源：
https://labuladong.gitbook.io/algo/di-ling-zhang-bi-du-xi-lie/dong-tai-gui-hua-xiang-jie-jin-jie
动态规划解题套路框架
"""

"""
理解：
首先是穷举所有可能的结果，在结果中寻找最优解
"""


def coin_change(coins: List[int], amount: int):

    @lru_cache()
    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            # 子问题无解，跳过
            if sub_problem == -1:
                continue
            # sub_problem + 1 意思是 sub 已经有解，在并且为计算结果加一
            res = min(res, 1 + sub_problem)

        return res if res != float('INF') else -1

    return dp(amount)


if __name__ == '__main__':
    coin_list = [1, 3, 5]
    print(coin_change(coin_list, 116))


