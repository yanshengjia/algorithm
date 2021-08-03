"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
 

Constraints:
* The number of nodes in the list is in the range [0, 100].
* 0 <= Node.val <= 100


Solution:
1. Recursive
2. Iterative
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Recursive
# TC: O(N), N = size(list)
# SC: O(N), stack space for recursion
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # no node or only 1 node left
        if head == None or head.next == None:
            return head
        
        # two nodes to be swapped
        first = head
        second = head.next
        
        # swap
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second


# Iterative
# TC: O(N)
# SC: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # pre node of head
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        
        while head and head.next:
            # nodes to be swapped
            first = head
            second = head.next
            
            # swap 2 nodes
            first.next = second.next
            second.next = first
            pre.next = second
        
            # reinitialize the head and pre node for the next swap
            pre = first
            head = first.next
        
        return dummy.next
        