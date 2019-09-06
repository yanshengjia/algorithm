"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

Solution:
1. Output the linked list to an array
Time: O(N), Space: O(N)
2. Reverse half of the linked list
Use fast and slow pointers to find the mid point, reverse the first half of the linked list, then compare the first half and the second half.
Time: O(N), Space: O(1)
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Output the linked list to an array
# Time: O(N), where N is the length of the linked list
# Space: O(N), since we store all the nodes' val of the linked list
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []
        while head != None:
            array.append(head.val)
            head = head.next
        
        l = len(array)
        if l == 0 or l == 1:
            return True
        
        for i in range(l // 2):
            if array[i] != array[l-i-1]:
                return False
        return True



# Reverse the first half
# Time: O(N), >85%, where N is the length of linked list
# Space: O(1)
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return True
        
        slow = fast = head
        dummy = None
        
        while fast != None and fast.next != None:
            fast = fast.next.next
            head = head.next    # head will stop at the head of the second half
            # reverse the first half
            # dummy will stop at head of the reversed first half
            n = slow.next
            slow.next = dummy
            dummy = slow
            slow = n
            
        if fast != None:    # the length of linked list is odd
            head = head.next    # we can ignore the head of reversed first and second half, since they are one node
        
        while dummy and head:
            if dummy.val != head.val:
                return False
            
            dummy = dummy.next
            head = head.next
        return True
