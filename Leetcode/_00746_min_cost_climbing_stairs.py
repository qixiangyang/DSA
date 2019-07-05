"""
Description:
Author:qxy
Date: 2019-07-04 14:07
File: 00746_min_cost_climbing_stairs 
"""

"""
数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:

输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
 示例 2:

输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
注意：

cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
"""
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:

    # val_list = []
    # for start1 in range(2):
    #     start1_score = 0
    #     start1_score += cost[start1]
    #     while start1 < len(cost)-1:
    #         tmp = cost[start1+1: start1+3]
    #         print(tmp)
    #         print(start1_score)
    #         if len(tmp) > 1:
    #             if tmp[0] == tmp[1]:
    #                 start1 += 2
    #                 start1_score += tmp[1]
    #             else:
    #                 min_cost = min(tmp)
    #                 start1 += tmp.index(min_cost)+1
    #                 start1_score += min_cost
    #         if len(tmp) == 1:
    #             start1 += 1
    #             # start1_score += tmp[0]
    #         if len(tmp) == 0:
    #             break
    #     val_list.append(start1_score)
    # return min(val_list)

    dp0, dp1 = cost[0], cost[1]

    for i in range(2, len(cost)):
        dpi = min(dp0 + cost[i], dp1 + cost[i])
        dp0, dp1 = dp1, dpi

    return min(dp0, dp1)

    # start2 = 1
    # start2_score = 0
    # start2_score += cost[start2]
    # while start2 < len(cost):
    #     tmp = cost[start2+1: start2+3]
    #     if len(tmp) == 0:
    #         break
    #     min_cost = min(tmp)
    #     start2 += tmp.index(min_cost)+1
    #     start2_score += min_cost
    # # print(start2_score)
    # return start1_score


# data = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
data = [0, 1, 2, 2]
n = minCostClimbingStairs(data)
print(n)