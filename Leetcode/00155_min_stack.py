"""
Description:
Author:qxy
Date: 2019-06-15 12:35
File: 00155_min_stack 
"""

"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return sorted(self.stack)[0]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())


"""
执行用时 :1244 ms, 在所有Python3提交中击败了14.01%的用户
内存消耗 :16.3 MB, 在所有Python3提交中击败了98.14%的用户
"""