"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

from typing import List
from functools import lru_cache


def maxProfit(prices: List[int]) -> int:

    profit = float("-inf")

    @lru_cache(maxsize=500)
    def p_f(start, end):
        return end - start

    for index, s in enumerate(prices):
        for e in prices[index+1:]:
            profit = max(profit, p_f(start=s, end=e))

    return profit if profit > 0 else 0


# print(maxProfit(prices=[7,1,5,3,6,4]))


def get_profit(prices):
    min_price = float('inf')
    profit = 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(p-min_price, profit)

    return profit

a = get_profit([7,6,4,3,1])
print(a)



