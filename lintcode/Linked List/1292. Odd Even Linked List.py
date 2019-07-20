"""
Description:
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

Solution:
开一个链表保存偶数节点，在原链表中删除所有偶数节点，最后拼接起来。
注意循环停止的条件。
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
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        if head == None or head.next == None:
            return head
        count = 1
        even_head = ListNode(0)
        even_head_guard = even_head
        odd_head_guard = head
        while head.next != None:
            even_head.next = head.next
            even_head = even_head.next
            if head.next.next == None:
                break
            head.next = head.next.next
            head = head.next
        even_head.next = None
        head.next = even_head_guard.next
        return odd_head_guard
