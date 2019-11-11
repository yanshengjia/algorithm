"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

Solution:
1. Recursion
2. Iteration
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Iteration
# Time: O(n), n is the length of linked list
# Space: O(1)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # empty list
        if head == None:
            return None
        
        # move cur node to m-th node
        pre, cur = None, head
        c = 1
        while c < m:
            pre = cur
            cur = cur.next
            c += 1
        
        # remember two positions of head and tail of the reversed sublist
        tail, con = cur, pre
        
        # reverse sublist, pre will be the new head
        for i in range(n- m + 1):
            cur.next, cur, pre = pre, cur.next, cur
        
        # relink
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
            

# Recursion
# Time: O(n)
# Space: O(n)
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head
     