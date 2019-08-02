"""
Write code to remove duplicates from an unsorted linked list.

Example 1:
Input: 1->2->1->3->3->5->6->3->null
Output: 1->2->3->5->6->null

Solution:
Use a hashtable to record the value of nodes when we scan the linked list.

Follow up:
How would you solve this problem if a temporary buffer is not allowed? In this case, you don't need to keep the order of nodes.
"""


"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


# Time-O(N), where N is the number of nodes in the linked list
# Space-O(N)
class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        dummy = head
        pre = ListNode(0)
        pre.next = head
        d = dict()
        while head != None:
            is_move = True
            if head.val not in d:
                d[head.val] = 1
            else:
                pre.next = head.next
                is_move = False
            if is_move:
                pre = pre.next
            head = head.next
        return dummy