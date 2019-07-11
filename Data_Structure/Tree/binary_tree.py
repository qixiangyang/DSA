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

    def stack_lvr(self):
        """利用栈实现中序遍历"""
        stack = []
        current = self.root
        while current or stack:

            while current:
                stack.append(current)
                current = current.lchild

            current = stack.pop()
            print(current.value, end=" ")
            current = current.rchild

    def stack_lrv(self):
        """利用栈实现后序遍历"""
        if self.root is None:
            return
        lrv_reverse_stack = []
        operate_stack = [self.root]
        while operate_stack:
            node = operate_stack.pop()
            lrv_reverse_stack.append(node)
            if node.lchild is not None:
                operate_stack.append(node.lchild)
            if node.rchild is not None:
                operate_stack.append(node.rchild)

        while lrv_reverse_stack:
            print(lrv_reverse_stack.pop().value, end=" ")


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        print(tree)
        tree.add(i)

    print("\n前序遍历结果：", end="")
    tree.recursion_vlr(tree.root)  # 0 1 3 7 8 4 9 2 5 6
    print("\n中序遍历结果：", end="")
    tree.recursion_lvr(tree.root)  # 7 3 8 1 9 4 0 5 2 6
    print("\n后序遍历结果：", end="")
    tree.recursion_lrv(tree.root)  # 7 8 3 9 4 1 5 6 2 0
    print("\n层次遍历结果: ", end="")
    tree.level_scan()  # 0 1 2 3 4 5 6 7 8 9
    print("\n利用栈实现前序遍历: ", end="")
    tree.stack_vlr()  # 0 1 2 3 4 5 6 7 8 9
    print("\n利用栈实现中序遍历: ", end="")
    tree.stack_lvr()  # 7 3 8 1 9 4 0 5 2 6
    print("\n利用栈实现后序遍历: ", end="")
    tree.stack_lrv()  # 7 8 3 9 4 1 5 6 2 0




