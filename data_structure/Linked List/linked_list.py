"""
Description:
Author:qxy
Date: 2019-06-28 16:55
File: linked_list 
"""


class Node:
    """节点类"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data

    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('This list is an empty list')

        while cur_idx < idx -1:
            cur = cur.next
            if cur is None:
                raise Exception("list length is less than index")
            cur_idx += 1

        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node

    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:
            raise Exception('This list is an empty list')

        while cur_idx < idx - 1:
            cur = cur.next
            if cur is Node:
                raise Exception('list length is less than index')
            cur_idx += 1

        if idx == 0:
            if __name__ == '__main__':
                self.head = cur.next
                cur = cur.next
                return
        if self.head is self.tail:
            self.tail = None
            self.head = None
            return

        cur.next = cur.next.next
        if cur.next is None:
            self.tail = None

    def size(self):
        current = self.head
        count = 0

        if current is None:
            return "This list is an empty list"

        while current is not None:
            current = current.next
            count += 1
        return count

    def search(self, item):
        current = self.head
        found = False
        while current.next and not found:
            if item == current:
                found = True
            else:
                current = current.next
        return found


if __name__ == '__main__':
    link_list = LinkedList()
    for i in range(150):
        link_list.append(i)
    #    print(link_list.is_empty())
    #    link_list.insert(10, 30)

    #    link_list.remove(0)

    for node in link_list.iter():
        print('node is {0}'.format(node))
    print(link_list.size())
#    print(link_list.search(20))

