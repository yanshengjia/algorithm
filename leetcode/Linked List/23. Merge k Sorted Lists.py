"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


Solution:
1. Brute force. Collect all values of nodes and sort
2. Compare one by one
3. Compare by Priority Queue
4. Divide and Conquer. Reuse mergeTwoList()
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Divide and Conquer
# Time Complexity: O(nklogk), where n is the average length of linked list, k is the number of linked lists. We can merge two sorted linked list in O(n) and sum up the merge process O(logk * nk) 
# Space Complexity: O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = len(lists)
        if l == 0:
            return None
        gap = 1
        while gap < l:
            for i in range(0, l - gap, gap * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+gap])
            gap *= 2
        return lists[0]
        
        
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


# Brute force
# Time: O(NlogN), where N is the total number of nodes
# Space: O(N)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        dummy = cur = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        self.nodes.sort()
        for x in self.nodes:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next


# Comparing with Priority Queue or heapq
# This code only works for Python2, in Python3 it will complain about '<' not supported between instances of 'ListNode' and 'ListNode'
# Time: O(Nlogk), where k is the number of linked list. Every pop and insertion to priority queue cose O(logk), finding the smallest value cose O(1)
# Space: O(N+k)
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []
        heapq.heapify(q)
        dummy = cur = ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(q, (l.val, l))

        while len(q) > 0:
            val, node = heapq.heappop(q)
            cur.next  = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, node))
        return dummy.next
        