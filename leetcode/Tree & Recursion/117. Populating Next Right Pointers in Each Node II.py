"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 
Example:

Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.


Solution:
1. BFS + Queue Level Order Traversal
2. Dummy Node Traversal O(1) space
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


# BFS
# Time: O(N), N is tree size
# Space: O(N)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        cur_level = [root]
        while cur_level:
            next_level = []
            
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            l = len(next_level)
            for i in range(l-1):
                next_level[i].next = next_level[i+1]
            
            if l > 0:
                cur_level = next_level
            else:
                break
        return root


# Level Order Traversal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
    
        queue = [root]
        next_level = []

        while queue:
            node = queue.pop(0)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if queue:   # queue is not empty means cur node is not tail
                node.next = queue[0]
            if not queue:
                # cur level traversal finish
                queue, next_level = next_level, queue
        return root


# Level Order Traversal
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        tail = root
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if node == tail:
                # travel to the tail node of cur level, update the tail
                tail = queue[-1] if len(queue) > 0 else None
                node.next = None
            else:
                node.next = queue[0]
        return root



# Dummy Node Traversal
# Time: O(N)
# Space: O(1)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0, None, None, None)   # point to head node of each level
        pre = dummy
        
        res = root
        while root:
            if root.left:
                pre.next = root.left
                pre = pre.next
            if root.right:
                pre.next = root.right
                pre = pre.next
            
            root = root.next
            
            if root == None: # meet the tail of cur level
                pre = dummy # point to the head node of next level
                root = dummy.next   # became the head node of next level
                dummy.next = None   # for the last level, break while loop
                
        return res
