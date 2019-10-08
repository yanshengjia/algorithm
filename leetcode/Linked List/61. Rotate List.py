"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


Solution:
1. Output the linked list to array. Rotate the array and build a new linked list.
2. Close the linked list to a circle, and then cut the edge between -k-1 node and -k node
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# close the linked list to circle, then cut
# Time: O(N), N is the length of linked list
# Space: O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        # clost the linked list to circle
        l = 1
        while head.next:
            head = head.next
            l += 1
        head.next = dummy.next
        
        k %= l
        
        # cut
        cur = dummy.next
        for i in range(l-k-1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        return new_head


# output linked list to array
# Time: O(N)
# Space: O(N)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        k %= len(arr)
        if k > 0:
            arr = arr[-k:] + arr[:len(arr)-k]
        dummy = ListNode(0)
        cur = dummy
        for a in arr:
            node = ListNode(a)
            cur.next = node
            cur = cur.next
        return dummy.next
