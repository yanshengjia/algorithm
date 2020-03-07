"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.


Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0


Solution:
Binary to Decimal
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Use a list to store bits, then convert to decimal
# Time: O(N), where N is the number of nodes in linked list
# Space: O(N)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bits = []
        while head:
            bits.append(head.val)
            head = head.next

        l = len(bits)
        res = 0
        for bit in bits:
            l -= 1
            res += bit * pow(2, l)
        return res
        

# Time: O(N)
# Space: O(1)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        while head:
            res = (2 * res + head.val)
            head = head.next
        return res