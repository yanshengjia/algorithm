"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


Solution:
1. Reverse List -> Add two numbers -> Reverse List
2. Output to array
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Reverse Twice
# Time: O(M+N), M, N are the lengths of l1, l2
# Space: O(1)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1, len1 = self.reverse_linked_list(l1)
        l2, len2 = self.reverse_linked_list(l2)
        
        if len1 > len2:
            long_l, short_l = l1, l2
            long_len, short_len = len1, len2
        else:
            long_l, short_l = l2, l1
            long_len, short_len = len2, len1
        
        # add two numbers
        carry = 0
        cur1, cur2 = long_l, short_l
        i = 0
        while i < short_len:
            s = (cur1.val + cur2.val + carry) % 10
            carry = (cur1.val + cur2.val + carry) // 10
            cur1.val = s
            tail = cur1
            cur1 = cur1.next
            cur2 = cur2.next
            i += 1
        
        while carry > 0 and i < long_len:
            s = (cur1.val + carry) % 10
            carry = (cur1.val + carry) // 10
            cur1.val = s
            tail = cur1
            cur1 = cur1.next
            i += 1
        
        if carry > 0:
            tail.next = ListNode(carry)
        
        res, _ = self.reverse_linked_list(long_l)
        return res
    
    def reverse_linked_list(self, head):
        length = 0
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
            length += 1
        return pre, length
        
        