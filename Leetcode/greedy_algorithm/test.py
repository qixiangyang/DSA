"""
Description:
Author:qxy
Date: 2019-06-15 14:52
File: test 
"""

"""
[0-1背包问题]
有一个背包，背包容量是M=150kg。有7个物品，物品不可以分割成任意大小。（这句很重要）
要求尽可能让装入背包中的物品总价值最大，但不能超过总容量。
物品 A B C D E F G
重量 35kg 30kg 6kg 50kg 40kg 10kg 25kg
价值 10 40 30 50 35 40 30

"""


class Item(object):
    def __init__(self, n, w, v):
        self.name = n
        self.weight = format(w)
        self.value = format(v)

    def getName(self):

        return self.name

    def getValue(self):

        return self.value

    def getWeight(self):

        return self.weight

    def __str__(self):
        result = '<' + self.name + ',' + str(self.value) + ',' + str(self.weight) + '>'
        return result


def value(item):
    return item.value


def weightInverse(item):
    return 1.0 / int(item.weight)


def density(item):
    return int(item.getValue())/int(item.getWeight())


def greedy(items, maxWeight, keyFucthion):
    itemCopy = sorted(items, key=keyFucthion, reverse=True)
    result = []
    totalweight = 0
    totalvalue = 0

    for i in range(len(itemCopy)):
        print(totalweight, itemCopy[i].getWeight(), maxWeight)
        if (totalweight + int(itemCopy[i].getWeight())) <= maxWeight:
            result.append(itemCopy[i])
            totalvalue += int(itemCopy[i].getValue())
            totalweight += int(itemCopy[i].getWeight())
    return (result, totalvalue)


def buildItem():
    names = ['A', 'B', 'C', 'D', 'E', 'F','G']
    vals = [35, 30, 6, 50, 40, 10, 25]
    weights = [10, 40, 30, 50, 35, 40, 30]
    Items = []
    for i in range(len(names)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items


def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken = ', val)
    for item in taken:
        print(' ', item)


def testGreedys(maxWeight=150):
    items = buildItem()

    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)

    print('\n Use greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)

    print('\n Use greedy by density to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)


testGreedys(maxWeight=150)
