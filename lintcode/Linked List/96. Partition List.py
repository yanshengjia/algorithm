"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input:  list = null, x = 0
Output: null	
Explanation: The empty list Satisfy the conditions by itself.

Solution:
Create two linked lists, one for smaller nodes, another for bigger nodes.
In the end, concat these two lists.
Dont forget about make the next pointer of last node in big linked list to None
p_big.next = None
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head == None:
            return head
        small_dummy, big_dummy = ListNode(0), ListNode(0)
        p_small, p_big = small_dummy, big_dummy
        while head != None:
            print(head.val)
            if head.val < x:
                p_small.next = head
                p_small = p_small.next
            else:
                p_big.next = head
                p_big = p_big.next
            head = head.next
        p_big.next = None
        p_small.next = big_dummy.next
        return small_dummy.next
