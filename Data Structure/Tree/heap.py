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
"""
堆的特点：
堆有两点需要了解，一是堆是一颗完全二叉树，完全二叉树就是只有最后一层有页子节点，而且页子节点是靠左排列的；
二是堆中的每一个节点都大于其左右子节点（大顶堆），或者堆中每一个节点都小于其左右子节点（小顶堆）。
"""


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

        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):

        self.data_list.append(data)
        index = len(self.data_list) - 1
        print(index)
        parent = self.get_parent_index(index)
        # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
        print(index, parent)

        while parent is not None and self.data_list[parent] < self.data_list[index]:
            # 交换操作
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(parent)

    def removeMax(self):
        """
        删除堆定元素
        """
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        # 堆化
        self.heapify(0)
        return remove_data

    def heapify(self, index: int):
        """
        从上往下堆化，从index 开始堆化操作 (大顶堆)
        """
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2*index + 1 <= total_index and self.data_list[2*index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index + 1
            if 2*index + 2 <= total_index and self.data_list[2*index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


if __name__ == "__main__":
    myheap = Heap()
    for i in range(10):
        myheap.insert(i+1)
    print('建堆:', myheap.data_list)
    print("删除堆顶元素：", [myheap.removeMax() for _ in range(10)])






