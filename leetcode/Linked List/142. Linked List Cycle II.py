"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Solution:
Hashtable
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Hashtable
# Time: O(n), where n is the length of linked list
# Space: O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = dict()  # key: node, value: index
        index = 0
        while head != None:
            if head not in d:
                d[head] = index
                index += 1
            else:
                return head
            head = head.next
        return None