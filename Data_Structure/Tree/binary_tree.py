"""
Description:
Author:qxy
Date: 2019-07-08 17:22
File: binary_tree 
"""


class Node(object):

    def __init__(self, value=None, lchild=None, rchlid=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchlid

    def __str__(self):
        return str(self.value)


class Tree(object):

    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, ele):
        new_node = Node(ele)
        self.queue.append(new_node)
        if self.root.value is None:
            self.root = new_node
        else:
            tree_node = self.queue[0]
            if tree_node.lchild is None:
                tree_node.lchild = new_node
            elif tree_node.rchild is None:
                tree_node.rchild = new_node
                self.queue.pop(0)

    def recursion_vlr(self, root: Node):
        """递归前序遍历"""
        if root is None:
            return
        print(root.value, end=" ")
        self.recursion_vlr(root.lchild)
        self.recursion_vlr(root.rchild)

    def recursion_lvr(self, root: Node):
        """递归中序遍历"""
        if root is None:
            return
        self.recursion_vlr(root.lchild)
        print(root.value, end=" ")
        self.recursion_vlr(root.rchild)

    def recursion_lrv(self, root: Node):
        """递归后序遍历"""
        if root is Node:
            return
        self.recursion_lvr(root.lchild)
        self.recursion_lvr(root.rchild)
        print(root.value, end=" ")

    def level_scan(self):
        queue = []
        start = self.root
        queue.append(start)
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.lchild is not None:
                queue.append(current.lchild)
            if current.rchild is not None:
                queue.append(current.rchild)

    def stack_vlr(self):
        """利用栈实现先序遍历"""
        stack = []
        current = self.root
        while current or stack:
            while current:
                print(current.value, end=" ")
                stack.append(current)
                current = current.lchild

            current = stack.pop()
            current = current.rchild





