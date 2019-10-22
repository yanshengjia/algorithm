"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:
You must return the copy of the given head as a reference to the cloned list.


Solution:
1. 2 pass Iteration with Hashtable O(N) space
2. 1 pass Iteration O(1) space
2. Recursion
"""


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

# 2 pass iteration with Hashtable
# key: original_node, value: new_node
# Time: O(N), where N is the size of linked list
# Space: O(N)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return None
        d = {}  # key: original_node, value: new_node
        
        cur = head
        while (cur):
            d[cur] = Node(cur.val, None, None)
            cur = cur.next
        
        cur = head
        while (cur):
            d[cur].next = d.get(cur.next, None)
            d[cur].random = d.get(cur.random, None)
            cur = cur.next
        
        return d[head]
