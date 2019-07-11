"""
Description:
Author:qxy
Date: 2019-07-10 14:11
File: heap 
"""

"""
url：https://www.jianshu.com/p/d174f1862601
"""

# from collections import deque
# L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
# L.appendleft(0)
#
# print(L)


class Heap(object):

    def __init__(self):
        """
        初始化一个空堆，使用数组来在存放堆元素，节省存储

        """
        self.data_list = []

    def get_parent_index(self, index):
        """
        返回父节点的下标
        :param index:
        :return:
        """

        if index == 0 or index > len(self.data_list) -1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):

        self.data_list.append(data)
        index = len(self.data_list) - 1

        while self.data_list:
            pass

