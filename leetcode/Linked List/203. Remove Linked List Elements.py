"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5


Solution:
Keep a pre pointer and cur pointer. Make sure that pre pointer is always prior to the cur pointer.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head != None:
            if head.val == val:
                while head.next != None and head.next.val == val:
                    head = head.next
                pre.next = head.next    # keep pre the prior node of head
            else:
                pre = pre.next
            head = head.next
        return dummy.next
