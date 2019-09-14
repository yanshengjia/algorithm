"""
Write a program to find the node at which the intersection of two singly linked lists begins.

Example1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Solution:
1. Hashtable
Traverse list A and store the address / reference to each node in a hash set. Then check every node bi in list B: if bi appears in the hash set, then bi is the intersection node.
2. Two Pointers
Maintain two pointers pA and pB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pB reaches the end of a list, redirect it the head of A.
把 list A 接到 list B 后 和 把 list B 接到 list A 后的长度是一样的，最后一个节点是相同的，可以反推到 intersection node 都是相同的。
让两个指针这么遍历，第一次相遇的点就是 intersection.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Hash Table
# Time: O(M+N), M, N is the length of list A,B
# Space: O(M) or O(N)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        d = set()
        while headA != None:
            d.add(headA)
            headA = headA.next
        
        while headB != None:
            if headB in d:
                return headB
            headB = headB.next
        

# Two Pointers
# Time: O(M+N)
# Space: O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        
        dummyA, dummyB = headA, headB
        while dummyA != dummyB:
            if dummyA == None:
                dummyA = headB
            else:
                dummyA = dummyA.next
            if dummyB == None:
                dummyB = headA
            else:
                dummyB = dummyB.next
        return dummyA
