"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...


Solution:
Iteration
Use two heads to maintain odd/even lists. Remember the dummy head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Time: O(n), n is the lenght of linked list
# Space: O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        d1 = odd = ListNode(0)
        d2 = even = ListNode(0)
        
        c = 1
        cur = head
        while cur:
            if c % 2:
                odd.next = cur
                odd = cur
            else:
                even.next = cur
                even = cur
            cur = cur.next
            c += 1
        
        # relink
        odd.next = d2.next
        even.next = None
        return d1.next
