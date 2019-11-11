"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

Solution:
[iterative] 三指针，一个存当前节点之前的节点，一个存当前节点，一个存当前节点之后的节点，对当前节点迭代

[recursion] nk.next.next = nk;
Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. This bug could be caught if you test your code with a linked list of size 2.
"""


# Iterative
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur != None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev


# Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)  # p is the last node
        print(p.val)
        head.next.next = head
        head.next = None
        return p


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Python 表达式先计算右值，右值都计算完毕，在从左往右给左值赋值
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre
