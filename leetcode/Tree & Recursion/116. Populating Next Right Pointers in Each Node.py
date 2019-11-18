"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Example:

Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":{"$id":"6","left":null,"next":null,"right":null,"val":6},"next":null,"right":{"$id":"7","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}

Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":{"$id":"6","left":null,"next":null,"right":null,"val":7},"right":null,"val":6},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"7","left":{"$ref":"5"},"next":null,"right":{"$ref":"6"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"7"},"val":1}

Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
 

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.


Solution:
Kind of like a linked list problem

node.left.next = node.right
if node.next:
    node.right.next = node.next.left

1. Recursion DFS
2. Iteration BFS/DFS
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


# BFS Iteration + Queue
# Time: O(N), N is tree size
# Space: O(N)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        queue = [] # (node, number_of_node (left-right, top-down))
        level = 2
        cnt = 1
        
        dummy = root
        # deal with first level
        if root.left:
            queue.append((root.left, cnt))
            cnt += 1
            queue.append((root.right, cnt))
            cnt += 1
            
        pre = None
        while queue:
            node1, num1 = queue.pop(0)
            node2, num2 = queue.pop(0)
            
            if pre:
                pre.next = node1
            node1.next = node2
            pre = node2
            
            # next level
            if num2 == 2**level - 2:
                level += 1
                pre = None
        
            if node1.left:
                queue.append((node1.left, cnt))
                cnt += 1
                queue.append((node1.right, cnt))
                cnt += 1
                queue.append((node2.left, cnt))
                cnt += 1
                queue.append((node2.right, cnt))
                cnt += 1
            
        return dummy     
        
        
# Recursion
def connect1(self, root):
    if root and root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)


# BFS + Queue
def connect2(self, root):
    if not root:
        return 
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)


# DFS + Stack
def connect(self, root):
    if not root:
        return 
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            stack.append(curr.right)
            stack.append(curr.left)
