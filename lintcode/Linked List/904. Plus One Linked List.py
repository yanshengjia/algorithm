"""
Desc:
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.

Example1:
Input: 1 -> 2 -> 3 -> null
Output: 1 -> 2 -> 4 -> null
Explanation:
123 + 1 = 124

Solution:
Scan the linked list to get the num, then add 1 and rebuild the linked list, this approach may cost more space
O(n) time complexity, O(n) space complexity, assume n is the length of the linked list.
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
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        num = 0
        while head != None:
            cur_val = head.val
            num = num * 10 + cur_val
            head = head.next
        num += 1
        num_list = list(str(num))
        
        dummy = ListNode(0)
        res = dummy
        for i in range(len(num_list)):
            val = num_list[i]
            node = ListNode(val)
            dummy.next = node
            dummy = dummy.next
        return res.next
