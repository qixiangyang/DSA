"""
Description:
Author:qxy
Date: 2019-06-09 11:44
File: dick_tesla 
"""


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        costs[n] = new_cost
        parents[n] = node

    processed.apped(node)