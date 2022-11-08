"""
https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_str = ""
    while True:
        l1_str += str(l1.val)
        if l1.next is None:
            break
        l1 = l1.next
    print(f"l1_str: {l1_str}")

    l2_str = ""
    while True:
        l2_str += str(l2.val)
        if l2.next is None:
            break
        l2 = l2.next

    print(f"l2_str: {l2_str}")

    big, small = l1_str, l2_str
    if len(l1_str) < len(l2_str):
        big, small = l2_str, l1_str

    total = int(big) + int(small)
    print(total)

    node_list = list()
    for s in str(total):
        node_list.append(ListNode(int(s)))

    for i, n in enumerate(node_list):
        if i + 1 <= len(node_list) - 1:
            n.next = node_list[i+1]

    return node_list[0]


if __name__ == '__main__':

    # test link table
    a1 = ListNode(2)
    b1 = ListNode(4)
    c1 = ListNode(3)
    a1.next = b1
    b1.next = c1

    a2 = ListNode(5)
    b2 = ListNode(6)
    c2 = ListNode(4)
    d2 = ListNode(6)
    a2.next = b2
    b2.next = c2
    c2.next = d2

    addTwoNumbers(a1, a2)

    # print(a.next.next.val)