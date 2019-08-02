"""
Insert a node in a sorted linked list.

Example 1:
Input: head = 1->4->6->8->null, val = 5
Output: 1->4->5->6->8->null

Solution:
while loop 找到仅次于 val 的节点位置
"""


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        dummy = ListNode(val)
        dummy.next = head
        p = dummy
        while p.next != None and p.next.val < val:
            p = p.next
        inserted = ListNode(val)
        inserted.next = p.next
        p.next = inserted
        return dummy.next
        