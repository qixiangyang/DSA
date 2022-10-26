"""
Description:
Author:qxy
Date: 2019-06-29 14:23
File: Queue 
"""


class Queue(object):

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]

    def enqueue(self, data):
        self.items.insert(0, data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
