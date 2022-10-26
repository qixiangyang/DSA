"""
Description:
Author:qxy
Date: 2019-06-29 14:16
File: Stack 
"""


class Stack(object):
    """
    栈
    """
    def __init__(self):
        self.item = []

    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        return self.item == []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)
