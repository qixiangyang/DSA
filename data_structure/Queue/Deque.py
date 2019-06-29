"""
Description:
Author:qxy
Date: 2019-06-29 14:41
File: Deque 
"""


class Deque(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, data):
        self.items.insert(0, data)

    def add_tail(self, data):
        self.items.append(data)

    def del_front(self):
        self.items.pop(0)

    def del_tail(self):
        self.items.pop()

    def size(self):
        return len(self.items)

