"""
Given a linked list, swap every two adjacent nodes and return its head.

Example 1:
Input: 1->2->3->4->null
Output: 2->1->4->3->null

Solution:
1. Swap val
2. Swap nodes
"""


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# swap val
# Time-O(N), where N is the length of the linked list
# Space-O(1)
class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        while head != None and head.next != None:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next
        return dummy.next


# swap nodes 把 dummy 要指向的头节点做成 tmp，这样 dummy.next 只会生效一次
# Time-0(N)
# Space-O(1)
class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next

